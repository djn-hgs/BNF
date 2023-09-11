import lark

command_grammar = '''
start: comment | command
command: print_command
        | for_command
        | assignment_command
        | comparison_command
        | increment_command

comment: "#"text

comparison_command: expression operator expression
assignment_command: let variable equals number
print_command: "print(" open_quote text close_quote ")"
for_command: "for(" space command semi_colon command semi_colon command ")"
increment_command: variable plus_plus

semi_colon: /\s*\;\s*/
equals: /\s*\=\s*/
operator: /\s*[\<,\>]\s*/
plus_plus: /\s*\+\+\s*/
let: /\s*let\s*/

text : CHARACTER | text CHARACTER
number: DIGIT | DIGIT number

variable: ALPHABETIC | ALPHABETIC variable_body
variable_body: VARIABLE_BODY | variable_body VARIABLE_BODY

expression: variable | number

open_quote: /\s*\"/
close_quote: /\"\s*/
space: " "*

DIGIT: "0".."9"
ALPHABETIC: "a".."z" | "A".."Z"
VARIABLE_BODY: "a".."z" | "A".."Z" | "0".."9" | "_"
CHARACTER: "a".."z" | "A".."Z" | " "
COMMENT: "#"
'''

p = lark.Lark(command_grammar, ambiguity="explicit")

tree = p.parse('for(let i = 0 ; i < 5 ; i ++ )')

print(tree.pretty())


