import requests
api_key=""
while True:
    bozulacak_para=input("Bozduracağınız para birimini giriniz (örneğin:USA): ")

    alinacak_para=input("Almak istediğiniz para birimini giriniz (örneğin:EUR): ")
    try:
        amount=int(input("Bozdurmak istediğiniz tutarı giriniz: "))
        break
    except ValueError:
        print("Tekrar deneyiniz.")

my_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{bozulacak_para}"

result=requests.get(my_url)
result=result.json()

new_amount=amount*result["conversion_rates"][alinacak_para]

print(f"{amount}{bozulacak_para}={new_amount}{alinacak_para}")