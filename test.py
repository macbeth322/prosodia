#!/usr/bin/env python

from itertools import chain

def parse_v1():
    import parser
    with open('full-bnf.bnf') as f:
        bnf = f.read()

    results = list(parser.Syntax.match(bnf))
    results = sorted(results, key=lambda a: len(a[0]))
    r = results[0][1]
    print(r.as_syntax())

def parse_v2():
    import parser_v2 as p
    with open('full-bnf.bnf') as f:
        bnf = f.read()
    lang = p.Language.create('Syntax')
    lang.add_rule(
        p.Rule(
            'Syntax',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Rules'),
                    p.EOFTerm()
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Rules',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Rule')
                ),
                p.TermGroup.create(
                    p.RuleReference('Rule'),
                    p.RuleReference('Rules')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Rule',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('OptWhitespace'),
                    p.Literal('<'),
                    p.RuleReference('RuleName'),
                    p.Literal('>'),
                    p.RuleReference('OptWhitespace'),
                    p.Literal('::='),
                    p.RuleReference('OptWhitespace'),
                    p.RuleReference('Expression'),
                    p.RuleReference('LineEnd')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'OptWhitespace',
            p.Syntax.create(
                p.TermGroup.create(
                    p.Literal(' '),
                    p.RuleReference('OptWhitespace')
                ),
                p.TermGroup.create(
                    p.Literal('')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Expression',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('List')
                ),
                p.TermGroup.create(
                    p.RuleReference('List'),
                    p.RuleReference('OptWhitespace'),
                    p.Literal('|'),
                    p.RuleReference('OptWhitespace'),
                    p.RuleReference('Expression')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'LineEnd',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('SingleLineEnd'),
                ),
                p.TermGroup.create(
                    p.RuleReference('SingleLineEnd'),
                    p.RuleReference('LineEnd'),
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'SingleLineEnd',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('OptWhitespace'),
                    p.Literal('\n')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'List',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Term')
                ),
                p.TermGroup.create(
                    p.RuleReference('Term'),
                    p.RuleReference('OptWhitespace'),
                    p.RuleReference('List')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Term',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Literal')
                ),
                p.TermGroup.create(
                    p.Literal('<'),
                    p.RuleReference('RuleName'),
                    p.Literal('>'),
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Literal',
            p.Syntax.create(
                p.TermGroup.create(
                    p.Literal('"'),
                    p.RuleReference('Text1'),
                    p.Literal('"'),
                ),
                p.TermGroup.create(
                    p.Literal("'"),
                    p.RuleReference('Text2'),
                    p.Literal("'"),
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Text1',
            p.Syntax.create(
                p.TermGroup.create(
                    p.Literal('')
                ),
                p.TermGroup.create(
                    p.RuleReference('Character1'),
                    p.RuleReference('Text1'),
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Text2',
            p.Syntax.create(
                p.TermGroup.create(
                    p.Literal('')
                ),
                p.TermGroup.create(
                    p.RuleReference('Character2'),
                    p.RuleReference('Text2'),
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Character',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Letter')
                ),
                p.TermGroup.create(
                    p.RuleReference('Digit')
                ),
                p.TermGroup.create(
                    p.RuleReference('Symbol')
                ),
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Letter',
            p.Syntax.create(
                *(
                    p.TermGroup.create(
                        p.Literal(letter)
                    ) for letter in chain(
                        (chr(ord('a') + offset) for offset in range(26)),
                        (chr(ord('A') + offset) for offset in range(26))
                    )
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Digit',
            p.Syntax.create(
                *(
                    p.TermGroup.create(
                        p.Literal(chr(ord('0') + offset))
                    ) for offset in range(10)
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Symbol',
            p.Syntax.create(
                *(
                    p.TermGroup.create(
                        p.Literal(symbol)
                    ) for symbol in r'| !#$%&()*+,-./:;>=<?@[\]^_`{}~'
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Character1',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Character')
                ),
                p.TermGroup.create(
                    p.Literal("'")
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'Character2',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Character')
                ),
                p.TermGroup.create(
                    p.Literal('"')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'RuleName',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Letter')
                ),
                p.TermGroup.create(
                    p.RuleReference('Letter'),
                    p.RuleReference('RuleEnd')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'RuleEnd',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('OneRuleEnd')
                ),
                p.TermGroup.create(
                    p.RuleReference('OneRuleEnd'),
                    p.RuleReference('RuleEnd')
                )
            )
        )
    )
    lang.add_rule(
        p.Rule(
            'OneRuleEnd',
            p.Syntax.create(
                p.TermGroup.create(
                    p.RuleReference('Letter')
                ),
                p.TermGroup.create(
                    p.RuleReference('Digit')
                ),
                p.TermGroup.create(
                    p.Literal('-'),
                    p.RuleReference('Letter')
                ),
                p.TermGroup.create(
                    p.Literal('-'),
                    p.RuleReference('Digit')
                )
            )
        )
    )
    return lang.parse(bnf)

tree = parse_v2()
