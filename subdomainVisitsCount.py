class Solution:
    def subdomainVisits(self, cpdomains):
        countPairedDomains = {}
        output = []

        for cp in cpdomains:
            #separate the count from the domain
            #"900 google.mail.com" -> ["900", "google.mail.com"]
            cp = cp.split(" ")

            #assign the domain as the key, with visits as the integer value
            if countPairedDomains.get(cp[1]):
                countPairedDomains[cp[1]] += int(cp[0])
            else:
                countPairedDomains[cp[1]] = int(cp[0])

            domains = cp[1]
            #split the domains into subdomains
            domains = domains.split(".")

            #insert the highest level domain into the dictionary
            if countPairedDomains.get(domains[-1]):
                countPairedDomains[domains[-1]] += int(cp[0])
            else:
                countPairedDomains[domains[-1]] = int(cp[0])

            #if there's 3 subdomains, we need to append the next level domain as well
            if len(domains) == 3:
                #combine the higher level domain and lower level domain into one
                # "mail" + "com" -> "mail.com"
                secondDomain = domains[-2] + '.' + domains[-1]
                
                if countPairedDomains.get(secondDomain):
                    countPairedDomains[secondDomain] += int(cp[0])
                else:
                    countPairedDomains[secondDomain] = int(cp[0])

        for pair in countPairedDomains.keys():
            #concatenate the value (cp count) with the domain name
            entry = str(countPairedDomains[pair]) + " " + pair
            output.append(entry)

        return output