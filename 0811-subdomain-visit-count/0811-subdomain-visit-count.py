from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        Slice the domain into subdomains
        1. Whole domain
        2. Second domain + third domain
        3. Third domain
        Store a hashmap of domain -> count
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