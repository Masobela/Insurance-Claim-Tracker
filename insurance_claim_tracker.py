customers={
    "Alice":{"policy_number": "INS1001","total_claims":0,"total_amount":0},
    "Bob":{"policy_number": "INS1002","total_claims":0,"total_amount":0},
    "Diana":{"policy_number": "INS1003","total_claims":0,"total_amount":0},
    "Charlie":{"policy_number": "INS1004","total_claims":0,"total_amount":0},  
}
claims = [
    {"customer": "Alice", "claim_amount": 5000,"claim_type":"accident"},
    {"customer": "Bob", "claim_amount": 12000,"claim_type":"health"},
    {"customer": "Charlie", "claim_amount": 8000,"claim_type":"property"},
    {"customer": "Alice", "claim_amount": 7000,"claim_type":"accident"},
    {"customer": "Diana", "claim_amount": 1000,"claim_type":"health"},
    {"customer": "Bob", "claim_amount": 3000,"claim_type":"accident"},
]

def process_claims(claim):
    customer = claim["customer"]
    amount = claim["claim_amount"]
    claim_type = claim["claim_type"]

    if customer in customers:
        customers[customer]["total_claims"] += 1
        customers[customer]["total_amount"] += amount 
    else:
         customers[customer] = {"policy_number": "NEW", "total_claims": 1, "total_amount": amount}
    if amount > 1000:
        print(f" High claim detected for {customer}: R {amount} ({claim_type})")
    else:
        print(f"{customer} made a {claim_type} claim of R {amount}")

for idx,claim in enumerate(claims, start= 1):
    print(f"\nProcessing claim #{idx}")
    process_claims(claim)

print("\n Customer Summary:")
names = list(customers.keys())
data = list(customers.values())

for name, info in zip(names, data):
    print(f"{name} | Policy: {info['policy_number']} | Total Claims: {info['total_claims']} | Total Amount: R {info['total_amount']}")