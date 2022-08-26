
import requests
import hashlib
import sys

def request_api_data(query_char):
   url='https://api.pwnedpasswords.com/range/'+query_char
   res=requests.get(url)
   

   if res.status_code != 200:
       raise RuntimeError(f'error fetching:{res.status_code},check the api and try again ')

   return res
 
def password_leak_count(hashes,hashes_to_check):
    hashes=(line.split(':')for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hashes_to_check:
            return count
    return 0


def pwned_api_checck(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    first5_char , tail=sha1password[:5] , sha1password[5:]
    print(first5_char,tail)
    Response=request_api_data(first5_char)
   
    return password_leak_count(Response,tail)
    
    

def main(args):
 for password in args:
     count=pwned_api_checck(password)
     if count:
         print(f'the password is used{count} times....use should change password')
     else:
        print(f'{password} was mot found good to go')

 return "done"


main(sys.argv[1:])
