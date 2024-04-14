import re

num_guests = int(input('Please enter number of guests to come?'))

vip_codes = set()
reg_codes = set()

for i in range(num_guests):
    r_code = input()

    # vip codes start with a digit while regulare codes start with character
    if re.match(r'^\d', r_code) and len(r_code) == 8:
        vip_codes.add(r_code)
    else:
        reg_codes.add(r_code)

all_codes = vip_codes | reg_codes

print(f'vip_codes: {vip_codes}')
print(f'reg_codes: {reg_codes}')
print(f'all_codes: {all_codes}')

arrived_vip = set()
arrived_reg = set()


while True:
    code = input()

    if code == 'END':
        print(len(all_codes) - len(arrived_vip) - len(arrived_reg))
        # first print vip who did not show up
        not_arrived_vip = vip_codes - arrived_vip
        not_arrived_reg = reg_codes - arrived_reg

        for vip in sorted(not_arrived_vip):
            print(vip)

        for reg in sorted(not_arrived_reg):
            print(reg)
        break

    if re.match(r'^\d', code) and len(code) == 8:
        arrived_vip.add(code)
        print(f'A vip guest arrived with a code: {code}')
    else:
        arrived_reg.add(code)
        print(f'A regular guest arrived with a code: {code}')
