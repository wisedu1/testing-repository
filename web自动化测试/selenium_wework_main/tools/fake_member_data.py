from faker import Faker
import yaml


# 中国化的 faker
faker = Faker(locale='zh_CN')
faker_members = []
# 创建 100 个 faker members
faker_members_num = 100
member_file_path = '../data/add_mem.yml'
for i in range(faker_members_num):
    temp_member = {'username': faker.name(), 'acctid': faker.credit_card_number(), 'phone': faker.phone_number()}
    faker_members.append(temp_member)

with open(member_file_path, 'w', encoding="utf-8") as yaml_file:
    yaml.dump(faker_members, yaml_file, default_flow_style=False, allow_unicode=True)
