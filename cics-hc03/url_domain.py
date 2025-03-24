
def main():
    # Input the URL from the user
    url = input("Enter a website URL (e.g., www.apple.com or hunter.edu): ")
    
    # Split the URL to get the domain parts
    if '.' in url:
        domain_parts = url.split('.')
        
        # Check if there are at least two parts to extract the website name and TLD
        if len(domain_parts) >= 2:
            website_name = domain_parts[-2] # get the second-to-last part of the domain, site name
            top_level_domain = domain_parts[-1] # get the last part of the domain, .com, .edu, etc.
            
            # Print the website name
            print(f"website name: {website_name}")
            
            # Determine the type of top level domain
            if top_level_domain == 'com':
                print("commercial")
            elif top_level_domain == 'edu':
                print("education")
            elif top_level_domain == 'org':
                print("organization")
            elif top_level_domain == 'gov':
                print("government")
            else:
                print("other")
        else:
            print("Invalid URL format. Please enter a proper URL.")

# call the main function to execute the program
if __name__ == "__main__":
    main()
