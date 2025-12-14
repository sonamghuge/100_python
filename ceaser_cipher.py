alphbet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        
def ceaser(original_text,shift_amount,encode_decode_amount):
    output_text=''
    if encode_decode_amount=='decode':
                shift_amount*=-1

    for letter in original_text:
        if letter not in alphbet:
            output_text+=letter
        else: 
            shift_position=alphbet.index(letter)+shift_amount
            shift_position%=len(alphbet)
            output_text+=alphbet[shift_position]
    print(f'here is the {encode_decode_amount} result:  {output_text}')

should_continue=True

while should_continue:
    direction=input('Type "encode" for encrypt, type "decode" for decrypt\n').lower()
    text=input('type your message\n').lower()
    shift=int(input('type the shift number\n'))

    ceaser(text,shift,direction)

    restart=input('Type "yes" if you want to continue. otherwise, type "no" ').lower()
    if restart=='no':
        should_continue=False
        print('goodby')



















# def encrypt(original_text,shift_amount):
#     cipher_text=''
#     for letter in original_text:
#         shift_position=alphbet.index(letter)+shift_amount
#         shift_position%=len(alphbet)
#         cipher_text+=alphbet[shift_position]
#     print(f'here is the encoded result:  {cipher_text}')

# def dencrypt(original_text,shift_amount):
#     output_text=''
#     for letter in original_text:
#         shift_position=alphbet.index(letter)-shift_amount
#         shift_position%=len(alphbet)
#         output_text+=alphbet[shift_position]
#     print(f'here is the decoded result:  {output_text}')
#encrypt(original_text=text,shift_amount=shift)
#dencrypt(original_text=text,shift_amount=shift)
