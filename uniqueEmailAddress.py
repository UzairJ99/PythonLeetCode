class Solution:
    def numUniqueEmails(self, emails):
        uniqueEmails = {}
        #count occurances of each email
        for email in emails:
            #format the email
            email = formatEmail(email)
            if uniqueEmails.get(email):
                uniqueEmails[email] += 1
            else:
                uniqueEmails[email] = 1
        #return number of unique emails
        return len(uniqueEmails)
    
def formatEmail(email):
    #split local and domain name
    email = email.split("@")
    #replace dots
    email[0] = email[0].replace(".", "")
    #trim upto +
    if '+' in email[0]:
        email[0] = email[0][:email[0].find('+')]
    #resync local and domain names
    email = '@'.join(email)
    print(email)
    return email