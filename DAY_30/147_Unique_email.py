'''Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3'''









# My logic 

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()

        for email in emails:
            loc = ""
            dom = ""
            ig = False
            ind = email.index('@')

            for i in range(ind):
                char = email[i]
                if ig:
                    continue
                if char == '.':
                    continue
                elif char == '+':
                    ig = True
                else:
                    loc += char

            for i in range(ind + 1, len(email)):
                dom += email[i]

            femail = loc + '@' + dom
            unique.add(femail)

        return len(unique)

















# Leet code best solution

# class Solution:
#     def numUniqueEmails(self, emails):
#         unique_emails = set()

#         for email in emails:
#             local, domain = email.split('@')
#             local = local.split('+')[0]
#             local = local.replace('.', '')
#             normalized_email = local + '@' + domain
#             unique_emails.add(normalized_email)

#         return len(unique_emails)