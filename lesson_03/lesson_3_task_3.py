from address import Address
from mailing import Mailing


from_address = Address('630001', '�����������', '������', '10', '5')
to_address = Address('101000', '������', '��������', '20', '15')

mailing = Mailing(from_address, to_address, 350, 'TRK123456789')

print(
    f'����������� {mailing.track} '
    f'�� {mailing.from_address.index}, '
    f'{mailing.from_address.city}, '
    f'{mailing.from_address.street}, '
    f'{mailing.from_address.house} - '
    f'{mailing.from_address.apartment} '
    f'� {mailing.to_address.index}, '
    f'{mailing.to_address.city}, '
    f'{mailing.to_address.street}, '
    f'{mailing.to_address.house} - '
    f'{mailing.to_address.apartment}. '
    f'��������� {mailing.cost} ������.'
)
