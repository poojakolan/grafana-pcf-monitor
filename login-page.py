import mechanize  #pip install mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]

sign_in = br.open("https://login.ham.cloud.8451.com/login")  #the login url

br.select_form(nr = 0)

br["username"] = "email/username" #the key "username" is the variable that takes the username/email value

br["password"] = "password"    #the key "password" is the variable that takes the password value

logged_in = br.submit()   #submitting the login credentials

logincheck = logged_in.read()  #reading the page body that is redirected after successful login

print logincheck #printing the body of the redirected url after login