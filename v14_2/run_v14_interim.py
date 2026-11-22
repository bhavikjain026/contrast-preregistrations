#!/usr/bin/env python3
"""Plan v14, addendum v14.2, section 4: the interim description from ONE coder's sheet (Kahan, sheet A).
This is not the registered result. The registered result is analyse_v14.py run once on the settled codes of both coders.

Usage, on the team lead's Mac, once, after Kahan hands in his sheet:
    python3 run_v14_interim.py <Kahan's sheet, as handed in, .xlsx>
Check of this script on made-up codes only (no real code is read, nothing is logged):
    python3 run_v14_interim.py --selftest

What it does, in order:
 1. Stops unless every fixed input matches its published SHA-256 (addendum v14.1 section 8, plan v14 section 11).
 2. Stops if the attempts log already holds a COMPLETE line, or if an output file exists.
 3. Copies the handed-in sheet into handed_in/ under a name that carries its hash, and logs STARTED.
 4. Converts it with sheet_to_codes.py, unchanged. If the converter refuses the sheet, logs REFUSED and stops; addendum
    v14.2 section 4 says the sheet then goes back to the coder with the converter's error lines only.
 5. Runs analyse_v14.py version 3, unchanged, with the interim label, and saves its output to interim_output.txt.
 6. Logs COMPLETE with the hashes of the codes file and the output. It prints hashes only, never the tables."""
import sys, os, hashlib, shutil, subprocess, platform, tempfile, random, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
FIXED = {
    'run/analyse_v14.py': '1ae10bdfcd67319cf6cc6f4a9346a54e10e86e9ffdb37fe3c9f6f67e36ccd88d',
    'run/sheet_to_codes.py': '900f96e04ee59f35829dce805efadc74b41cd1bfe96a529fb1dd50599152e0f2',
    'run/KEY_lead_only.csv': '784371443a21b4e22e40484b487c9deddfe7772a6546930a82fa28b97388c1a2',
    'run/coding_sheet_coder_A.xlsx': '585d267e8b5edfa914e73cb7b243bb6b472f9802739ea33c95fab189bba6d500',  # the blank sheet as sent
    'tutorstudy_v5/items.csv': '0c61ddb332212e4ee683a2ca6a2d601ab82790377432f6a94d7a0c18722ca395',
}
LABEL = 'INTERIM: one coder (Kahan, sheet A), codes not settled; addendum v14.2 section 4; NOT the registered result'
LOG, OUT, ERR = 'interim_attempts.log', 'interim_output.txt', 'interim_error.txt'
CODES_JSON = 'codes_kahan_interim.json'


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 16), b''): h.update(b)
    return h.hexdigest()


def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def log(base, line):
    with open(os.path.join(base, LOG), 'a') as f: f.write(f'{line} | {now()}\n')


def check_fixed(base):
    bad = [f for f, h in FIXED.items() if not os.path.isfile(os.path.join(base, f)) or sha(os.path.join(base, f)) != h]
    if bad: raise SystemExit('STOP: these inputs are missing or do not match their published SHA-256: ' + ', '.join(bad))


def run(base, sheet):
    check_fixed(base)
    logp = os.path.join(base, LOG)
    if os.path.exists(logp) and any(l.startswith('COMPLETE') for l in open(logp)):
        raise SystemExit('STOP: the attempts log already holds a COMPLETE line. The interim run happens once.')
    for f in (OUT, ERR):
        if os.path.exists(os.path.join(base, f)): raise SystemExit(f'STOP: {f} already exists. Do not delete it; ask the team lead.')
    if not os.path.isfile(sheet): raise SystemExit(f'STOP: no file at {sheet}')
    h = sha(sheet)
    if h == FIXED['run/coding_sheet_coder_A.xlsx']: raise SystemExit('STOP: this is the blank sheet as sent, not a coded sheet.')
    os.makedirs(os.path.join(base, 'handed_in'), exist_ok=True)
    kept = os.path.join(base, 'handed_in', f'coding_sheet_coder_A_kahan_{h[:16]}.xlsx')
    if not os.path.exists(kept): shutil.copy2(sheet, kept)
    if sha(kept) != h: raise SystemExit('STOP: the kept copy does not match the handed-in sheet.')
    rund = os.path.join(base, 'run')
    log(base, f'STARTED sheet {h} | python {platform.python_version()} on {platform.system()}')
    r = subprocess.run([sys.executable, 'sheet_to_codes.py', kept, CODES_JSON], cwd=rund, capture_output=True, text=True)
    if r.returncode:
        n = r.stderr.count('\n  ') or 1
        log(base, f'REFUSED by sheet_to_codes.py, {n} error line(s); nothing analysed')
        print(r.stderr.strip()); print('\nREFUSED. Send Kahan only the error lines above (row and rule). Nothing was analysed.')
        if os.path.exists(os.path.join(rund, CODES_JSON)): os.remove(os.path.join(rund, CODES_JSON))
        return 2
    r = subprocess.run([sys.executable, 'analyse_v14.py', CODES_JSON, LABEL], cwd=rund, capture_output=True, text=True)
    if r.returncode:
        open(os.path.join(base, ERR), 'w').write(r.stderr)
        log(base, f'FAILED in analyse_v14.py, exit {r.returncode}; error saved to {ERR}')
        print(f'FAILED. The error is in {ERR}. Addendum v14.2 section 4: a dated addendum comes before any second run.')
        return 3
    head = (f'{LABEL}\nSheet as handed in: SHA-256 {h}\nCodes file: {CODES_JSON}, SHA-256 {sha(os.path.join(rund, CODES_JSON))}\n'
            f'analyse_v14.py version 3, unchanged: SHA-256 {FIXED["run/analyse_v14.py"]}\nRun {now()}, python {platform.python_version()} on {platform.system()}\n\n')
    open(os.path.join(base, OUT), 'w').write(head + r.stdout)
    log(base, f'COMPLETE codes {sha(os.path.join(rund, CODES_JSON))} output {sha(os.path.join(base, OUT))}')
    print(f'COMPLETE. Output saved to {OUT} (SHA-256 {sha(os.path.join(base, OUT))}). Kept private: addendum v14.2 section 4.')
    return 0


def made_up_sheet(base, dest, rows=198, seed=1):
    """A copy of the blank sheet with made-up codes in every row. No real code is used."""
    from openpyxl import load_workbook
    wb = load_workbook(os.path.join(base, 'run', 'coding_sheet_coder_A.xlsx')); ws = wb['Coding']; rng = random.Random(seed)
    codes = ['OTHER', 'NAMES-BOTH', 'PRESUMES', 'PRESUMES-THEN-CHECKS', 'ASKS-HOW', 'NO-DIAGNOSIS']
    calcs = ['hit rate', 'base rate', '100 minus false-alarm rate', 'hit rate minus false-alarm rate', 'base rate times hit rate']
    done = 0
    for row in ws.iter_rows(min_row=2):
        if row[0].value is None: continue
        if done >= rows: row[0].value = None; continue
        row[3].value = rng.choice(codes)
        if row[3].value in ('NAMES-BOTH', 'PRESUMES', 'PRESUMES-THEN-CHECKS'):
            row[4].value = rng.choice(calcs); row[5].value = rng.choice(['FITS', 'DOES-NOT-FIT'])
        done += 1
    wb.save(dest)


def selftest():
    tmp = tempfile.mkdtemp(prefix='v14_interim_selftest_')
    for f in FIXED:
        os.makedirs(os.path.dirname(os.path.join(tmp, f)), exist_ok=True); shutil.copy2(os.path.join(HERE, f), os.path.join(tmp, f))
    fake = os.path.join(tmp, 'made_up.xlsx'); made_up_sheet(tmp, fake)
    assert run(tmp, fake) == 0
    out = open(os.path.join(tmp, OUT)).read()
    assert out.startswith(LABEL) and f'=== {LABEL}: plan v14 section 7 ===' in out and 'Stratum B' in out
    print(f'selftest passed on made-up codes in {tmp}')
    return tmp


def main(argv, base=HERE):
    if argv == ['--selftest']: selftest(); return 0
    if len(argv) != 1: raise SystemExit(__doc__)
    if platform.system() != 'Darwin': raise SystemExit("STOP: the interim run is made on the team lead's Mac (Darwin).")
    return run(base, os.path.abspath(argv[0]))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
