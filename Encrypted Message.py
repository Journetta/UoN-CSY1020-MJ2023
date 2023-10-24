import base64

coded_string = ("bWVzc2FnZSA9ICAoIkhlbGxvIFdvcmxkISIpCkF0dGVtcHQ9aW5wdXQoIldoYXQgaXMgeW91ciBwYXNzd29yZD8gIikKcGFzc3dvcmQgPSAoIkJhbmFuYSIpCmlmIEF0dGVtcHQ9PXBhc3N3b3JkOgogICAgcHJpbnQgKG1lc3NhZ2UpCmVsc2U6CiAgICBwcmludCAoIiIpCgo=")
decoded_bytes = base64.b64decode(coded_string)
decoded_string = decoded_bytes.decode("utf-8")
code = open ("Encrypt.py", 'w')
code.write (decoded_string)
code.close()
import Encrypt
#if Encrypt.Attempt == Encrypt.password:
 #   change = input("Keep your Password? (Yes/No")
  #  if change != "yes":
   #         print ("Okay Good Bye!")
    #else:
     #       takepass = input("What is your new password?")
      #      print ("Ur New Password is!" + takepass)
       #     Encrypt.password = takepass
