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

            domains = []
            domains.append(domain)

            # If in format rep d1.d2.d3, extract d2.d3
            split_domains = domain.split(".")
            if len(split_domains) > 2:
                second_third_domain = split_domains[1] + "." + split_domains[2]
                domains.append(second_third_domain)
            
            # For both formats rep d1.d2 and rep d1.d2.d3, extract d2 and d3 respectively
            domains.append(split_domains[-1])
            
            for d in domains:
                domain_to_count[d] += int(count)
        return [str(count) + " " + domain for domain, count in domain_to_count.items()]