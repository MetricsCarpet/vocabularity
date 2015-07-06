import enchant

text = "This is sme text with a fw speling errors in it."
d = enchant.Dict("en_US")   # create dictionary for US English
print d.check("enchant")

print d.check("enchnt")
print d.suggest("enchnt")
['enchant', 'enchants', 'enchanter', 'penchant', 'incant', 'enchain',
 'enchanted']
