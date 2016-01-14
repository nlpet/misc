
from random import choice, randint

'''
Non-deterministic finite state machine
a) All strings over {a,b} that contain bba but not aab
b) All strings over {a,b} that contain neither bab nor aab.
'''


class NFSM:

    # Starting point
    def start(self):
        self.steps(self.start_state)

    # End point
    def end(self, current_state):
        if current_state in self.accepting:
            self.tests[self.test_num].append('PASS')
        else:
            self.tests[self.test_num].append('FAIL')
        self.tests[self.test_num].append(self.state_trace)

    # Execute steps between states
    def steps(self, step):
        self.state_trace.append(step)
        if self.is_last_char():
            self.end(step)
        else:
            letter = self.current_string[self.current_index]
            self.current_index += 1
            next_steps = self.transitions[step][letter]
            if next_steps:
                if len(next_steps) == 1:
                    next_step = next_steps[0]
                elif len(next_steps) > 1:
                    next_step = choice(next_steps)
                self.steps(next_step)
            else:
                self.end(step)

    # Run n number of tests
    def run_tests(self, tests=10, errors_only=False):
        self.tests = {}
        for t in range(1, tests + 1):
            self.test_num = t
            self.current_string = self.generate_random_string()
            self.state_trace = []
            self.tests[self.test_num] = ["".join(self.current_string)]
            self.current_index = 0
            self.start()
        self.print_test_results(errors_only)

    # Display test results
    def print_test_results(self, errors_only):
        print '\n\t----- Test results for {} -----\n'.format(self.name)
        stats = {'pass': 0, 'fail': [[], 0]}
        for k, v in self.tests.items():
            expected = self.validate_string(v[0])
            ok = 'OK' if expected == v[1] else 'ERROR'
            if ok == 'OK':
                stats['pass'] += 1
            else:
                stats['fail'][0].append(k)
                stats['fail'][1] += 1

            if not errors_only:
                formatter = '{1:%d}' % self.max_string_len
                to_print = '#{0:3}: %s --> {2} == {3} | {4}' % formatter
                print to_print.strip().format(
                    k, v[0], v[1], expected, ok
                )
        if not errors_only:
            print ''
        print 'Stats:'
        print '{} passed; {} failed\n'.format(stats['pass'], stats['fail'][1])

        if stats['fail'][0]:
            print 'Failed tests:'
            for n in stats['fail'][0]:
                test = self.tests[n]
                print '#{0:3}: {1:21} ({2}) | trace:  {3}'.format(
                    n, test[0], test[1], "->".join(test[2])
                )
            print ''

    # Determine whether a string should be accepted or not
    def validate_string(self, s):
        for req in self.required:
            if s.find(req) == -1:
                return 'FAIL'
        for forb in self.forbidden:
            if s.find(forb) >= 0:
                return 'FAIL'
        return 'PASS'

    # Generate a random string for testing, duplicates are probable
    # with a high number of tests
    def generate_random_string(self):
        chars = []
        for _ in range(randint(self.min_string_len, self.max_string_len)):
            chars.append(choice(self.alphabet))
        return chars

    def is_last_char(self):
        return self.current_index == len(self.current_string)


class NFSMA(NFSM):
    def __init__(self, min_string_len=1, max_string_len=20):

        assert min_string_len > 0, "Min string length must be at least 1"
        self.min_string_len = min_string_len
        self.max_string_len = max_string_len

        # Name of finite state machine
        self.name = 'NFSM (A)'
        # All states of the machine
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4',
                       'q5', 'q6', 'q7', 'q8', 'q9']
        # Allowed transitions between states
        self.transitions = {
            'q0': {'a': ['q1'], 'b': ['q2']},
            'q1': {'a': [], 'b': ['q2']},
            'q2': {'a': ['q1'], 'b': ['q3']},
            'q3': {'a': ['q4'], 'b': ['q3']},
            'q4': {'a': ['q5', 'q7'], 'b': ['q8']},
            'q5': {'a': ['q5'], 'b': ['q6']},
            'q6': {'a': [], 'b': []},
            'q7': {'a': ['q5'], 'b': ['q6']},
            'q8': {'a': ['q9'], 'b': ['q8']},
            'q9': {'a': ['q7'], 'b': ['q8']}
        }
        # The allowed characters
        self.alphabet = ['a', 'b']
        # Start state
        self.start_state = 'q0'
        # States accepted as success
        self.accepting = ['q4', 'q5', 'q7', 'q8', 'q9']

        # Forbidden and required substrings
        self.forbidden = ['aab']
        self.required = ['bba']

        # Keeping track of current string
        self.current_string = []
        self.current_index = 0


class NFSMB(NFSM):
    def __init__(self, min_string_len=1, max_string_len=20):

        assert min_string_len > 0, "Min string length must be at least 1"
        self.min_string_len = min_string_len
        self.max_string_len = max_string_len

        # Name of finite state machine
        self.name = 'NFSM (B)'
        # All states of the machine
        self.states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
        # Allowed transitions between states
        self.transitions = {
            'q0': {'a': ['q1'], 'b': ['q3']},
            'q1': {'a': ['q2', 'q4'], 'b': ['q1']},
            'q2': {'a': ['q2'], 'b': ['q5']},
            'q3': {'a': ['q2'], 'b': ['q3']},
            'q4': {'a': ['q2', 'q4'], 'b': ['q5']},
            'q5': {'a': [], 'b': []},
        }
        # The allowed characters
        self.alphabet = ['a', 'b']
        # Start state
        self.start_state = 'q0'
        # States accepted as success
        self.accepting = ['q1', 'q2', 'q3', 'q4']

        # Forbidden and required substrings
        self.forbidden = ['bab', 'aab']
        self.required = []

        # Keeping track of current string
        self.current_string = []
        self.current_index = 0


if __name__ == '__main__':
    m1 = NFSMA(1, 50)
    m1.run_tests(500, True)

    m2 = NFSMB(1, 50)
    m2.run_tests(500, True)
