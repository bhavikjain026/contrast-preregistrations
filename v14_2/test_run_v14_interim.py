"""Tests for run_v14_interim.py on MADE-UP codes only. Run: python3 test_run_v14_interim.py"""
import os, shutil, sys, tempfile, contextlib, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_v14_interim as R

ok = 0
def check(cond, what):
    global ok
    if not cond: raise SystemExit('FAILED: ' + what)
    ok += 1

def layout():
    tmp = tempfile.mkdtemp(prefix='v14_interim_test_')
    for f in R.FIXED:
        os.makedirs(os.path.dirname(os.path.join(tmp, f)), exist_ok=True); shutil.copy2(os.path.join(R.HERE, f), os.path.join(tmp, f))
    return tmp

def stops(fn):
    try:
        with contextlib.redirect_stdout(io.StringIO()): fn()
    except SystemExit as e: return str(e)
    return None

def quiet(fn):
    with contextlib.redirect_stdout(io.StringIO()): return fn()

# 1. Selftest: a full pass on made-up codes writes the labelled output and a COMPLETE line.
t = quiet(R.selftest)
log = open(os.path.join(t, R.LOG)).read()
check(log.count('STARTED') == 1 and log.count('COMPLETE') == 1, 'one STARTED and one COMPLETE line')
check(os.path.isfile(os.path.join(t, 'run', R.CODES_JSON)), 'codes file written')
check(len(os.listdir(os.path.join(t, 'handed_in'))) == 1, 'one kept copy of the sheet')
# 2. A second run is refused.
check('COMPLETE line' in (stops(lambda: R.run(t, os.path.join(t, 'made_up.xlsx'))) or ''), 'second run refused')
# 3. A changed fixed input stops the run.
t2 = layout(); open(os.path.join(t2, 'run/analyse_v14.py'), 'a').write('\n# changed\n')
check('run/analyse_v14.py' in (stops(lambda: R.run(t2, 'x.xlsx')) or ''), 'changed analysis script stops the run')
# 4. The blank sheet is refused as input.
t3 = layout()
check('blank sheet' in (stops(lambda: R.run(t3, os.path.join(t3, 'run/coding_sheet_coder_A.xlsx'))) or ''), 'blank sheet refused')
# 5. A sheet that breaks the converter's rules (197 rows) is REFUSED, nothing analysed, and a corrected sheet can still run.
t4 = layout(); bad = os.path.join(t4, 'bad.xlsx'); R.made_up_sheet(t4, bad, rows=197)
check(quiet(lambda: R.run(t4, bad)) == 2, 'short sheet returns 2')
check('REFUSED' in open(os.path.join(t4, R.LOG)).read() and not os.path.exists(os.path.join(t4, R.OUT)), 'REFUSED logged, no output')
check(not os.path.exists(os.path.join(t4, 'run', R.CODES_JSON)), 'no codes file left after a refusal')
good = os.path.join(t4, 'good.xlsx'); R.made_up_sheet(t4, good)
check(quiet(lambda: R.run(t4, good)) == 0, 'corrected sheet runs after a refusal')
# 6. The real run refuses to start off the Mac. The platform is faked as Linux, and the run is pointed at a temporary
#    layout, never at the real folder, so nothing real can run even if the guard were missing.
real_system = R.platform.system
t5 = layout(); fake = os.path.join(t5, 'made_up.xlsx'); R.made_up_sheet(t5, fake)
try:
    R.platform.system = lambda: 'Linux'
    msg = stops(lambda: R.main([fake], base=t5)) or ''
finally:
    R.platform.system = real_system
check('Darwin' in msg, 'Darwin guard stops the run off the Mac')
check(not os.path.exists(os.path.join(t5, R.LOG)), 'nothing logged when the guard stops the run')
# 7. The real folder was not touched by the tests.
check(not os.path.exists(os.path.join(R.HERE, R.LOG)) and not os.path.exists(os.path.join(R.HERE, R.OUT)), 'real folder untouched')
print(f'all {ok} checks passed (made-up codes only)')
