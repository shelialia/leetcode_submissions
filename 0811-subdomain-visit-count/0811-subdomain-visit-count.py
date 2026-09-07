from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        Store a hashmap of domain -> count
        Loop thru cpdomains:
        1. Split into count, domain
        2. Split domain into parts
        3. Loop through such that we take 1+2+3 -> 2+3 -> 3 based on length of parts
        - Join the parts using "."
        - Increment count on the domain
        """
        domain_to_count = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            parts = domain.split(".")

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                domain_to_count[subdomain] += int(count)

        return [
            f"{count} {domain}"
            for domain, count in domain_to_count.items()
        ]