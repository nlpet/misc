/*

### Lexical Scope

var is used to denote a variable which is Lexically Scoped to the current
function:

    function someFunc() {
      var aVariable;
    }

aVariable is lexically scoped within someFunc

### Block Scope

let & const are used to denote variables which are Block Scoped to the
current curly braced block:

    if (true) {
      let aVariable;
    }

aVariable is block scoped within the if's curly braces

-------------------------------------------------------------------------------

# Your Mission

In an empty file, create a function foo which contains one variable lexically
scoped named bar.

Once complete, execute scope-chains-closures verify <your-file.js> to verify your
solution.

## Notes

  * [1]: There are also 4 other scopes in the language: Global, `with`, `catch`,
  *      and `eval`. These tend not to be used much, so we will ignore them.
  *
  *
  * [2]: This workshop will concentrate only on Lexical Scoping.

*/

function foo() {
  var bar;
}
