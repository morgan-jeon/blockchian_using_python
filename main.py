from blockchain import Blockchain

blo = Blockchain()
blo.add_block({'Name':'Morgan'})
blo.add_block({'Name':'Minti'})
blo.add_block({'Name':'Tandae'})
print(blo.validate_chain())
blo.chain[2].transaction['Name'] = 'Minini'
print(blo.validate_chain())