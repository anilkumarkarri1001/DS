
Install a package:
pip install package_name

Uninstall a package:
pip uninstall package_name

Upgrade a package: 
pip install --upgrade package_name

List installed packages: 
pip list

Check your pip version:
pip --version

Pip Installs Packages 
Preferred Installation Program
========================================================================>
Request comes
     ↓
1. Middleware BEFORE
     ↓
2. API is processing
     ↓
3. API creates response
     ↓
4. Middleware AFTER
     ↓
Response goes to client

So the important rule is:

Code before await self.app(...) → runs BEFORE the request reaches the API.

Code after await self.app(...) → runs AFTER the API has processed the request.

await self.app(scope, receive, send)

basically means:
"Now pass this request to the next application layer and wait until it finishes."

So:
print("BEFORE")
await self.app(scope, receive, send)
print("AFTER")

========================================================================>
Python file = a container that can contain many different things. 📦   
Python file
│
├── Variables
├── Functions
├── Classes
├── Imports
├── Constants
└── Other Python code

========================================================================>
1. What is Encryption?
Encryption means:
Converting normal readable data (plain text) into an unreadable format
(encrypted/cipher text) using an encryption algorithm and a key.

Example:
Original data
    ↓
"Anil123"
    ↓
   🔐 Encryption
    ↓
"8fK2@xP91..."

The encrypted value looks meaningless to someone who doesn't have the required key.

Real-world example

Imagine you write:

My password is 12345

You put it inside a locked box:

"My password is 12345"
          ↓
       🔒 LOCK
          ↓
     "X7@k92Lm..."

That locking process is similar to encryption.


2. What is Decryption?
Decryption is the opposite.
It means:
Converting encrypted/unreadable data back into the original readable data using the appropriate key.
Encrypted data
     ↓
"8fK2@xP91..."
     ↓
    🔓 Decryption
     ↓
"Anil123"
So:
Encryption = Lock 🔒
Decryption = Unlock 🔓

========================================================================>

========================================================================>

 raise DepartmentExistsError(name)
plan = plan_role_addition(role_name, rec["custom_roles
========================================================================>
Defensive programming means:
Writing code in a way that expects possible problems and handles them safely 
instead of assuming everything will always work correctly.

Think of it like wearing a seat belt. 🚗
You don't expect an accident, but you prepare for one just in case.
Simple coding example

Without defensive programming:
def divide(a, b):
    return a / b
What happens if:
divide(10, 0)
💥 Error: division by zero.
With defensive programming:
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
Now the code expects that someone might give 0 and handles it safely.

========================================================================>
_LEGACY_STAFF_ROLES అంటే చాలా simple గా:
"పాత (old) staff roles" అని అర్థం.
ఇక్కడ ప్రతి పదం:
_ → సాధారణంగా internal/private variable అని సూచించడానికి Pythonలో ఉపయోగిస్తారు.
LEGACY → పాతది / గతంలో ఉపయోగించినది
STAFF_ROLES → Staff roles / ఉద్యోగుల పాత్రలు
ex : _LEGACY_STAFF_ROLES = {"Admin", "SuperAdmin", "Employee", "Supervisor", "Cashier"} 
========================================================================>
def set_department_head(session, dept_id: str,

========================================================================>
hmac.compare_digest(token, active)

"hmac.compare_digest() securely compares two secret values, "
"such as a token sent by the client and a token stored on the server."
" If both values match, it returns True; otherwise it returns False. "
"The function itself does not generate the token."   

========================================================================>
"Both are mature relational databases. "
"The choice depends on the application's requirements,"
" existing ecosystem, team expertise, and database features needed."

========================================================================>
11. Interview answer

If an interviewer asks:

"How can an application redirect a user to their previous page after login?"

You can answer:

"The frontend can preserve the originally requested route or last visited route,"
" for example using a return URL, router state, or browser storage."
" After successful authentication, the frontend reads that route and navigates the user back to it. "
"Alternatively, the application may use role-based default routing,"
" where the backend returns the user's role and the frontend chooses the appropriate landing page."



1. Most common reason — frontend remembers the last route
Suppose your URL is:
https://example.com/users/roles
When you logout, the application may clear your authentication token:
localStorage
   ↓
remove access_token

But it may not clear the current route.
The frontend might have something like:
currentRoute = "/users/roles"

After login, the application says:
Login successful
       ↓
Where should I navigate?
       ↓
Last/previous route
       ↓
/users/roles

So you are taken back there.
if login successful:     
navigate(previousRoute)   


3. Another possibility — localStorage
The frontend may store something like:
localStorage.setItem(
    "lastVisitedPage",
    "/users/roles"
);

========================================================================>
Term	Meaning	Example

Sign Up	Create a new account (Registration)	You enter your name, email, password → account is created
Sign In	Enter an existing account (Login)	You enter your email + password → you access your account

🧠 Easy way to remember

Sign Up = First time → Create account 🆕
Sign In = Already have account → Enter account 🔑

So:
Sign Up = Registration
Sign In = Login
========================================================================>
A company doesn't necessarily make money by charging the user directly.
 It can provide a free product to attract a huge number of users and make money from other 
 parts of the business.   


1. First understand the basic business model
I
magine I create an app called "AnilTube".

I tell you:

"Use it completely free!"
You might ask:
"Then how does AnilTube make money?"

There are several possibilities:
Model 1 — Advertisements

Companies pay me:
"Show our advertisement to your users."

Example:
You use a free app.
100 million people use it.

A company pays the app company to show advertisements to those users.
So:
Users → Free service
Advertisers → Pay company
Company → Pays developers + servers + other expenses
Company → Keeps remaining money as profit

2. Google is a great example 

Google provides many products for free:
 Google Search 
 Gmail 
 Chrome 
 Google Maps 
 YouTube 
 Google Photos (with limits) 
 Google Drive (with limits) 

You
 ↓
Use Google Search FREE
 ↓
Google has millions/billions of users
 ↓
Businesses want to reach those users
 ↓
Businesses pay Google for advertising
 ↓
Google earns revenue 

1,000 developers

Each developer needs:
Salary
Laptop
Office/infrastructure
Internet
Benefits
etc.

Google also needs:
Servers
Databases
Storage
Networking
Security
Data centers
Electricity
Monitoring
Customer support

All of this costs money.

Google earns revenue from various businesses, including advertising and paid products/services.

That revenue is used to pay those expenses.
Simplified:
                 GOOGLE
                    |
       ┌────────────┴────────────┐
       ↓                         ↓
    Revenue                   Expenses
       |                         |
       ↓                         ↓
 Advertising                Developer salaries
 Cloud                      Servers
 YouTube subscriptions      Data centers
 Google Workspace           Security
 Other services             Operations
       |
       ↓
 Remaining money
       |
       ↓
     Profit 

Because Gmail is part of the Google ecosystem.
For example:

You have:
Gmail
↓
Google Drive
↓
Google Docs
↓
Google Calendar
↓
Google Meet
↓
Google Search
↓
YouTube

6. What about WhatsApp? => statues rlated to products 



































DISTINCT is applied to the entire combination of columns returned, not only to mobile.
Your query returns:
RETURN DISTINCT
    sub.mobile AS mobile,
    sub.user_id AS user_id,
    sub.first_name AS first_name,
    sub.last_name AS last_name,
    sub.role AS role
Think of each result as a complete row:
mobile	user_id	first_name	last_name	role
9876	U001	Ravi	Kumar	Employee
9876	U001	Ravi	Kumar	Employee
9876	U001	Ravi	Kumar	Manager
9999	U002	Anil	Kumar	Employee
DISTINCT compares the whole row.


=============================================>
Click any line → immediately see who last changed that line, when, and which commit.   
Steps
1. Open Extensions
Press:
Ctrl + Shift + X
2. Search for:
GitLens
3. Install GitLens — Git supercharged
After installation, restart/reload the editor if asked.   
========================================================================>

1. First understand what a "slab" is

Imagine your incentive system has these slabs:
Lead Type	Min Count	Max Count	Rate
HOT	1	10	100
HOT	11	20	150
HOT	21	30	200
HOT	31	None	250

This means:

1  - 10       → Rate 100
11 - 20       → Rate 150
21 - 30       → Rate 200
31 onwards    → Rate 250

Here None for max_count means:

There is no upper limit.

So:
31, 32, 33, 100, 1000


all belong to the last slab.
Call:

slab_for(15, "HOT", slabs)

Flow:
n = 15
lead_type = HOT
        ↓
Find HOT slabs
        ↓
1 - 10       ❌
11 - 20      ✅
21 - 30      ❌
31 onwards   ❌
        ↓

Return 11 - 20 slab

Result:
{
    "lead_type": "HOT",
    "min_count": 11,
    "max_count": 20,
    "rate": 150
}



table  ; IncentivePlan 

def db_list_plans(session, period: Optional[str], status: Optional[str]) -> List[dict]:
    where, params = [], {}
    if period:
        where.append("p.period = $period"); params["period"] = period
    if status:
        where.append("p.status = $status"); params["status"] = status
    q = "MATCH (p:IncentivePlan) "
    if where:
        q += "WHERE " + " AND ".join(where) + " "
    q += "RETURN p ORDER BY p.created_at DESC"
    return [dict(r["p"]) for r in session.run(q, **params)]
========================================================================>
In your project, an Incentive Plan is basically a set of rules used to reward employees/marketing staff for achieving certain targets.
Think of it as:
"If you achieve this much work, you will get this reward."
Simple real-world example
Suppose a Marketing Manager creates this plan:
Incentive Plan: September 2026
Lead Type: HOT
1–10 leads    → ₹100 per lead
11–20 leads   → ₹150 per lead
21–30 leads   → ₹200 per lead
31+ leads     → ₹250 per lead
So if an employee generates 25 HOT leads, the system can determine which incentive slab applies.
Why was it introduced?
Without an incentive plan, the application would have to use hard-coded rules such as:
if leads <= 10:
    incentive = 100
elif leads <= 20:
    incentive = 150
That becomes difficult when the business changes the incentive rules.
Instead, the business can create a plan:
Marketing Manager
       ↓
Create Incentive Plan
       ↓
Define Slabs
       ↓
Define Prize Tiers
       ↓
System stores the rules
       ↓
Later calculate employee incentives
So the main purpose is to make incentive rules configurable and manageable through the application, rather than hard-coding them into Python.



========================================================================>
1. Privacy Policy = “What happens to your information?”
It explains how the company handles your personal data.

For example:

What information is collected?
Name
Mobile number
Email
Location
Photos

Why is it collected?
How is it stored?
Who can access/share it?
How can you request or control your data?

Privacy policies are intended to disclose a company's data practices; companies can also have legal obligations to honor privacy promises they make.

Simple example:
"We collect your mobile number to send OTPs and verify your account."

That belongs in the Privacy Policy.

2. Terms & Conditions = “What are the rules for using our app?”

This explains the rules between you and the company when you use the service.

For example:
You must provide correct information.
You cannot misuse the application.
You cannot create fraudulent accounts.
What happens if you violate the rules?
Who owns the app/content?
What are the responsibilities of the company and user?

How disputes are handled.
Think of it as:
"If you use our application, these are the rules you agree to follow."

Easy way to remember
Document	Main question
Privacy Policy	🔐 What happens to my data?
Terms & Conditions	📜 What are the rules for using the app



========================================================================>
To exit
Simply press:
q
That's it. You should return to:
PS C:\Users\DELL\OneDrive\Desktop\markwave_live_services>
Useful keys while inside git show
Key	Meaning
q	Exit
↑ / ↓	Move up/down
Space	Next page
b	Previous page
/text	Search for text



========================================================================>
In Antigravity IDE, using the GitLens extension,
 how can I search for my commits using commit IDs or author (@me), 
 view the matching commit messages in the Search & Compare section, 
 inspect the selected commit using GitLens Inspect, and compare the old code with the new code : 


Ctrl + Shift + P
        ↓
GitLens: Search Commits
        ↓
Search:
    #4d7a947       → search by commit ID
    @Anil Kumar    → search by author
    @me             → your commits
        ↓
Search & Compare
        ↓
Commit messages/results are displayed
        ↓
Select the commit
        ↓
GitLens Inspect
        ↓
Commit Details
        ↓
Changed Files
        ↓
Click a changed file
        ↓
OLD CODE  ↔  NEW CODE

========================================================================>
to get the all the commits names using the user name :

PS C:\Users\DELL\OneDrive\Desktop\markwave_live_services> git log --author="Anil Kumar" --oneline
4d7a947 (HEAD -> user_details_encryption, origin/user_details_encryption) added the middleware to encrypt responses
f90d9b4 user details n=encryption and decryption
PS C:\Users\DELL\OneDrive\Desktop\markwave_live_services>      

========================================================================>

Dear Manager and Project Manager,

I would like to acknowledge that I have received the following office equipment for my official work:

Laptop : M1(mackbook pro)
Serial Number :  FVFGN333Q05N
Configuration : 16 GB

I confirm that I received all the above items in good condition and will use them for official project-related work.

Thank you for providing the necessary equipment and support.

Kind regards,
Anil kumar Karri(AnimalKart Team).


========================================================================>

calculator-settings/active
CalculatorSettingsModel


The maximum request timeout limit for a Google Cloud Run service is 60 minutes (3,600 seconds),
 with a default setting of 5 minutes (300 seconds).Key Details on Request TimeoutsConfigurable Range: 
    You can set the request timeout anywhere from 1 to 3,600 seconds


A coupon is a special offer that gives a customer some kind of discount or benefit when buying something.
🛒 Simple real-world example
Imagine you go to a clothing shop.
A shirt costs:
₹1,000
The shop gives you a coupon:
COUPON: SAVE100
The coupon gives you ₹100 discount.
So:
Original price       = ₹1,000
Coupon discount      = ₹100
-----------------------------
Final price          = ₹900
You pay ₹900 instead of ₹1,000.
🤔 Why are coupons introduced?
Businesses introduce coupons mainly to encourage customers to buy.
For example:
Without coupon:
Customer → "₹1,000 is expensive. I'll think about it." ❌
With coupon:
Customer → "Oh! I can get ₹100 off. I'll buy it." ✅

def generate_invoice
========================================================================>

========================================================================>


@router.get("/visits", summary="List Farm/Office visits scoped by the caller's role")
async def list_visits(
    x_caller_mobile: Optional[str] = Header(None),
    verified_mobile: Optional[str] = Depends(get_verified_mobile),
    from_date: Optional[str] = Query(None, description="Filter by visit from_datetime (ISO), not the lead's upload date"),
    to_date: Optional[str] = Query(None, description="Filter by visit from_datetime (ISO), not the lead's upload date"),
    visit_type: Optional[Literal["Farm Visit", "Office Visit"]] = Query(None, description="Filter to one visit type; omit for both"),
    visited: Optional[bool] = Query(None, description="true = gate-checked-in already happened, false = scheduled but not yet checked in, omit = both"),
    executive_mobile: Optional[str] = Query(None, description="Restrict to one executive within the caller's scope (e.g. for a Marketing Manager drilling into one team member)"),
    search: Optional[str] = Query(None, description="Match against the lead's name, mobile, or email"),
    page: Optional[int] = Query(None, ge=1, description="1-indexed page number. Omit (with page_size) for the full unpaginated list."),
    page_size: Optional[int] = Query(None, ge=1, le=500, description="Items per page (max 500). Omit (with page) for the full unpaginated list."),
) -> Dict[str, Any]:
    """Every lead currently or previously scheduled for a Farm/Office visit,
    for reporting: how many leads visited vs. are still scheduled, split by
    visit type, over any date range — with each visit's owning executive and
    full lead details attached (via db_enrich_assignees, same as GET /leads).

    Scoped exactly like GET /leads: a Marketing Manager sees their whole
    subtree, a Marketing Lead sees their own scope, a Marketing Executive
    sees only visits for leads assigned to them.
    """
    x_caller_mobile = resolve_caller_mobile(x_caller_mobile, verified_mobile)
    driver = get_shared_driver()
    with driver.session() as session:
        roles = db_roles(session, x_caller_mobile)
        # Admin/SuperAdmin -> 'org'; marketing roles keep their own scoping;
        # any other STAFF role reads the whole report. is_staff is resolved
        # only when it can change the answer, so a marketing caller costs no
        # extra query.
        mode = visit_scope_mode(roles, is_staff=False)
        if mode == "none":
            require_staff(session, x_caller_mobile)   # 403 unless staff
            mode = "org"

        subtree = get_subtree(session, x_caller_mobile) if mode == "all" else []
        mobiles = [x_caller_mobile] + [m["mobile"] for m in subtree]
        filters = {
            "from_date": from_date, "to_date": to_date,
            "visit_type": visit_type, "visited": visited,
            "executive_mobile": executive_mobile, "search": search,
        }
        visits = db_list_visits(session, mobiles, mode, x_caller_mobile, filters)

        counts = {
            "total": len(visits),
            "farm_visits": sum(1 for v in visits if v.get("visit_type") == "Farm Visit"),
            "office_visits": sum(1 for v in visits if v.get("visit_type") == "Office Visit"),
            "visited": sum(1 for v in visits if v.get("visited")),
            "not_visited": sum(1 for v in visits if not v.get("visited")),
        }

        total_count = len(visits)
        paginate = page is not None or page_size is not None
        p = page or 1
        ps = page_size if page_size is not None else total_count
        if paginate:
            start = (p - 1) * ps
            visits = visits[start:start + ps]
        total_pages = 1 if ps <= 0 else max(1, -(-total_count // ps))

        db_enrich_assignees(session, visits)

    return {"statuscode": 200, "status": "success",
            "count": len(visits), "total_count": total_count,
            "page": p, "page_size": ps, "total_pages": total_pages,
            "counts": counts, "visits": visits}
========================================================================>
8. Interview answer
Q: What is APIRouter in FastAPI?
APIRouter is used to group related API endpoints and keep the FastAPI application modular and organized.
Q: What is prefix?
Prefix adds a common path to all routes inside a router. For example, /payouts makes /history become /payouts/history.
Q: What are tags?
Tags are mainly used to group and organize endpoints in Swagger/OpenAPI documentation.
Q: What is payouts.router?
It refers to the router object defined inside the payouts module.
Q: What does include_router() do?
It registers the routes from an APIRouter with the main FastAPI application.


6. Put everything together
Suppose your payouts.py contains:
from fastapi import APIRouter
router = APIRouter(
    prefix="/payouts",
    tags=["Payouts"]
)
@router.get("/history")
def get_history():
    return {"message": "Payout history"}
@router.post("/create")
def create_payout():
    return {"message": "Payout created"}
And your main.py contains:
from routers import payouts
app.include_router(payouts.router)
The result is:
                    FastAPI
                       │
                       │
              include_router()
                       │
                       ↓
                payouts.router
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
       /payouts/history    /payouts/create
             │                   │
             └─────────┬─────────┘
                       ↓
                    Swagger
                     /docs
                       │
                       ↓
                   Payouts

========================================================================>
deleting a node along with the realtionships 
MATCH (n:FirstDuePayOut)
detach delete n

========================================================================>

The problem is simply that Git branch names cannot contain spaces.
You tried:
git checkout -b "due payout details"
Git sees the spaces and rejects the branch name.
Use hyphens or underscores instead
For your task, I recommend:
git checkout -b due-payout-details
Or:
git checkout -b due_payout_details
========================================================================>

 idempotent create/update behavior means what in telugu idempotentn
Idempotent అంటే తెలుగులో సింపుల్‌గా:
ఒకే operation ని ఎన్నిసార్లు చేసినా, చివరికి result ఒకటే ఉండటం.
🔹 Simple example
Suppose API:
PUT /users/101
Body:
{
  "name": "Anil",
  "age": 22
}
ఈ APIని ఒక్కసారి call చేస్తే:
User 101 → Anil, 22
మళ్లీ అదే request:
User 101 → Anil, 22
మళ్లీ 10 times చేసినా:
User 101 → Anil, 22
Result మారదు.
👉 ఇదే idempotent behavior.


when we are returning response we should always return the reposnse in this format only :

return {
            "statuscode": 500,
            "status": "error",
            "message": str(e),
        } 

return {
            "statuscode": 200,
            "status": "success",
            "message": user deatils updated or created successfully,
        } 


raise HTTPException(
    status_code=500,
    detail='Internal error'
)

output :
{
     "detail":'Internal error'
}


| విషయం                           | Meaning                                                         | Simple memory                |
| ------------------------------- | --------------------------------------------------------------- | ---------------------------- |
| **Caste/Community Certificate** | మీరు ఏ communityకి చెందినవారో చూపిస్తుంది                       | "నేను ఏ community?"          |
| **OBC**                         | మీ community OBC categoryలో ఉందని చూపిస్తుంది                   | "నా category OBC"            |
| **OBC-NCL**                     | OBC + Non-Creamy Layer eligibility                              | "OBC + NCL"                  |
| **Financial Year**              | 1 Apr → 31 Mar income period                                    | "Income earn చేసే period"    |
| **Assessment Year**             | Old tax systemలో previous FY incomeకి సంబంధించిన following year | "Old system assessment year" |
| **Tax Year**                    | New systemలో 1 Apr → 31 Mar tax period                          | "New system's year"          |



Sure. This line looks complicated because of the for and tuple syntax, but the idea is very simple.
for name, value in (("from_date", from_date), ("to_date", to_date)):
Simple meaning
It means:
Take these two pairs one by one, and put the first value into name and the second value into value.


strip() అంటే తెలుగులో “అవసరం లేని ముందు/వెనుక ఖాళీలను తొలగించడం” అని అర్థం.
Python లో:
name = "   Anil Kumar   "
name = name.strip()
print(name)
Output:
Anil Kumar




 Apps like Uber, Rapido, food-delivery apps, and some package-tracking systems
   don't need you to manually refresh because the server can push new information to your app.'
   '
Uber has publicly described moving from polling/refreshing toward bi-directional streaming
 for real-time experiences. Its developer documentation also shows periodic driver-location updates 
 containing latitude, longitude, heading, and timestamp


1. Real-life example

Suppose you order biryani.

You see:
📍 Restaurant
🛵 Delivery boy
🏠 Your home

The delivery boy starts moving.

His phone might continuously obtain something like:
7:30:00
Latitude: 17.4400
Longitude: 78.3900

7:30:04
Latitude: 17.4410
Longitude: 78.3910

7:30:08
Latitude: 17.4420
Longitude: 78.3920

Those coordinates are sent to the backend.

Your phone receives the latest coordinates and moves the delivery-bike marker.

2. Very simple architecture
        DELIVERY BOY
        Mobile App
             │
             │ GPS location
             ↓
       ┌─────────────┐
       │   Backend   │
       │             │
       │ Location    │
       │ Service     │
       └──────┬──────┘
              │
              │ real-time push
              ↓
        CUSTOMER APP
              │
              ↓
        🛵 Marker moves

This happens continuously while the order/trip is active.

3. What happens inside the delivery boy's phone?
'
'The phone has GPS/location services.
'
'For example:
'
'GPS
 ↓
17.4400, 78.3900

The delivery app takes this information.

It may send something similar to:
{
    "delivery_id": "D123",
    "latitude": 17.4400,
    "longitude": 78.3900,
    "timestamp": 123456789
}


The exact implementation varies by company, but this is the basic idea.

Uber's documented location events similarly contain coordinates, direction/bearing and timestamps.
'
'The customer app doesn't continuously refresh the page. A persistent real-time connection such as WebSocket or streaming is used so that the backend can push new location events to the customer whenever the driver's location changes  
'
'
'10. Why Redis is useful
'
'Imagine you have:
10 lakh active delivery people
You frequently need:
"Where is delivery boy D45 RIGHT NOW?"

You don't necessarily want to query a heavy relational database every few seconds.
Instead:

Redis
 ↓
D45 → current lat/lon
Fast lookup.
And when a new location arrives:

OLD
17.4400, 78.3900
        ↓ update
NEW
17.4410, 78.3910

For live tracking, the current location is often more important than storing every single GPS point in the main transactional database.

11. What about the ETA?
This is another interesting part.
Suppose:
Delivery boy
     🛵
      ↓
      ↓ 3.2 km
      ↓
     🏠
Backend/map-routing systems can calculate things like:
Distance = 3.2 km
ETA = 12 minutes
As the location changes:
3.2 km → 2.8 km → 2.3 km → 1.7 km → 800 m
ETA can also be recalculated.
So you see:
12 min
 ↓
10 min
 ↓
8 min
 ↓
5 min
 ↓
2 min


9. Where does Kafka come into this?

At large scale, there can be thousands or millions of location updates.

For example:
Delivery Boy 1 → location
Delivery Boy 2 → location
Delivery Boy 3 → location
Delivery Boy 4 → location
...
Delivery Boy 1 → location
Delivery Boy 2 → location

Handling all this directly through one server is difficult.

A message/streaming system such as Kafka can be used to distribute the incoming events.

Conceptually:
                 ┌── Location Service
                 │
Drivers → Gateway → Kafka
                 │
                 ├── Matching Service
                 │
                 └── Analytics

Important: Kafka isn't required for every real-time application. '
'It's one possible component when scale and event processing require it
















GPS stands for Global Positioning System. 
It is a satellite-based positioning system that allows a receiver such as a smartphone to 
determine its position and precise time. It works by receiving signals from multiple 
satellites and calculating the receiver's position based on the signal travel times. '
'Applications such as navigation, ride-sharing, delivery tracking, logistics, emergency services '
'and surveying use this location information.  '
''
'
GPS gives the location. The map gives the meaning of that location.
"GPS gives me Google Maps."  
GPS  ↓ "I am at latitude X, longitude Y"  ↓ Map  ↓ "This coordinate is Madhapur, Hyderabad"  ↓ Routing  ↓ "Take this road to reach Gachibowli"     
GPS
Where am I?
Map
What is at this location?
Routing
How do I get from A → B?
Traffic system
Which route is currently faster?  
1. What problem did GPS solve?
Imagine there is no GPS.
You are in Hyderabad and someone tells you:
"Go to a new village 150 km away."
You have a few problems:
 Where exactly am I? 
 Which road should I take? 
 Am I going in the correct direction? 
 Where is the destination? 
 How far away am I? 
 How long will it take? 
 If I get lost, how can someone find me? 
Humans historically used landmarks, maps, compasses, stars, road signs, etc. GPS made it possible for a device to determine its position, navigation information, and precise time using satellite signals. 
🧠 The core problem GPS solves:
"I need to know WHERE something is."
That's the intuition you should remember.
2. What exactly is GPS?
GPS = Global Positioning System.
It is a system of satellites + ground control + receivers.
Your phone contains a GPS receiver.
Satellites continuously broadcast signals containing information about their position and precise time. Your phone receives signals from multiple satellites and calculates its own position. 
Very simplified:
        🛰️ Satellite
             \
              \
        🛰️ ---- 📱 Your phone
              /
             /
        🛰️
Your phone asks mathematically:
"Based on the signals I received from these satellites, where am I?"
3. The intuition — imagine 3 friends
Forget satellites for a moment.
Imagine three friends are standing at known locations:
Friend A 📍
          \
           \
            📱 You
           /
          /
Friend B 📍
       Friend C 📍
Friend A tells you:
"You are 5 km away from me."
Friend B:
"You are 7 km away from me."
Friend C:
"You are 3 km away from me."
Using those distances, you can narrow down your position.
GPS does something conceptually similar, except the reference points are satellites, and the distances are calculated from the travel time of their radio signals. A GPS receiver normally uses signals from at least four satellites to solve for position and time. 
4. Why does GPS need satellites?
Because satellites provide known reference points around Earth.
Think:
             🛰️
              |
              |
🛰️ -------- 🌍 -------- 🛰️
              |
              |
             🛰️
The satellites know:
My position = X
My time     = Y
Your phone receives their signals.
Then it calculates:
Satellite 1 → distance from me
Satellite 2 → distance from me
Satellite 3 → distance from me
Satellite 4 → distance from me
From those measurements:
             ↓
       📱 Your phone
             ↓
Latitude
Longitude
Altitude
Time
The FAA explains that the receiver uses the signal's travel time to estimate distance from the satellites and uses four satellites to determine latitude, longitude, altitude and time. 
5. What if GPS didn't exist?
This is where the concept becomes very easy.
Imagine today's world without GPS.
🚕 Uber/Rapido
Driver says:
"I don't know exactly where the passenger is."
Passenger says:
"I'm standing somewhere near this building."
The system has much less precise location information.
Today:
Passenger
   ↓
📱 Location
   ↓
Backend
   ↓
Driver
The driver can see where the passenger is.
🍔 Food delivery
Without location:
Customer:
"Come to my house."
Delivery person:
"Where exactly?"
Customer:
"Near the blue building."
😅
With location:
Customer 📍
      ↓
Backend
      ↓
Delivery person 🛵
The delivery person can navigate to the customer's location.
🗺️ Google Maps
Without positioning:
You:
"Where am I on this map?"
The map knows the roads, but your phone needs a way to determine your current position.
GPS provides the positioning information; mapping software then puts that position onto a digital map. 
So remember:
GPS gives the location. The map gives the meaning of that location.
6. Very important distinction for interviews
Don't say:
"GPS gives me Google Maps."
❌ Not exactly.
Think:
GPS
 ↓
"I am at latitude X, longitude Y"
 ↓
Map
 ↓
"This coordinate is Madhapur, Hyderabad"
 ↓
Routing
 ↓
"Take this road to reach Gachibowli"
There are multiple systems working together.
GPS
Where am I?
Map
What is at this location?
Routing
How do I get from A → B?
Traffic system
Which route is currently faster?
7. Real-world use cases
GPS is much bigger than Google Maps.
🚗 1. Navigation
Car
 ↓
GPS
 ↓
Current location
 ↓
Navigation app
 ↓
Route
Used in cars, bikes, aircraft, ships, etc. GPS is widely used for land, sea and air navigation. 
🛵 2. Uber / Rapido
Driver phone
    ↓
GPS
    ↓
Current location
    ↓
Backend
    ↓
Customer app
This enables location-based matching and live tracking.
🍕 3. Food delivery
Delivery partner
      ↓
GPS location
      ↓
Backend
      ↓
Customer
You can see approximately where your delivery partner is.
📦 4. Package tracking
GPS/location technologies can support package tracking and logistics/supply-chain management. 
For example:
Truck 🚚
 ↓
Location
 ↓
Logistics backend
 ↓
Tracking system
🚑 5. Emergency services
Suppose someone needs an ambulance.
Instead of:
"I'm somewhere near this road."
The system can obtain location information and help responders identify where assistance is needed.
GPS is used in emergency response to help locate vehicles and people and reduce dispatch delays. 
✈️ 6. Aviation
Aircraft use satellite navigation systems for positioning and navigation. GPS is one of the major GNSS systems used for this purpose. 
🚢 7. Ships
A ship in the ocean doesn't have buildings and road signs everywhere.
🌊 🌊 🌊 🌊
      🚢
🌊 🌊 🌊 🌊
GPS provides positioning information.
10. What happens if GPS is unavailable?
This is a good interview edge case.
Suppose the delivery boy goes somewhere with poor GPS reception.
The application may have difficulty obtaining an accurate GPS position.
Modern phones can also use other location sources such as Wi-Fi and cellular networks as part of broader location services. For example, Android's Emergency Location Service can combine GPS, Wi-Fi and cellular information. 
So don't think:
No GPS = phone has absolutely no idea where it is.
Instead:
GPS
 +
Wi-Fi
 +
Cellular
 +
Other sensors
       ↓
Location service
The exact combination depends on the device and application.






















Good — now we can clearly see the problem.
1. Your changes are still in the working directory
git status says:
modified: routers/order_tracking.py
modified: routers/purchases.py
So the previous git stash did not leave your working tree clean.
That's why Git still refuses:
git checkout farmincentives
because routers/purchases.py would be overwritten.
2. You have many stashes
You currently have:
stash@{0}
stash@{1}
stash@{2}
stash@{3}
stash@{4}
...
stash@{8}
It looks like you repeatedly clicked/ran Stash in VS Code, creating multiple stash entries.
The important one from your earlier command is:
stash@{4}: On due_payout_details: WIP due payout details
The newer ones are:
stash@{0}: WIP on due_payout_details: ca4de56 added onboarded details in due payouts
stash@{1}: WIP on due_payout_details: ca4de56 added onboarded details in due payouts
...
Don't pop/apply any stash yet
Because your current working directory still has changes, don't run:
git stash pop
or:
git stash apply
yet.
First, let's identify which stash contains your latest changes.
Run:
git stash show --stat stash@{0}
then:
git stash show --stat stash@{1}
and:
git stash show --stat stash@{4}
You should get something like:
 routers/order_tracking.py | ...
 routers/purchases.py      | ...
Most important
Do not delete any stash.
Also don't run:
git reset --hard
because your changes are valuable.
Once we identify the correct stash, we can safely do:
current changes
       ↓
make working tree clean
       ↓
switch to farmincentives
       ↓
do your work there
       ↓
switch back to due_payout_details
       ↓
restore your due-payout work
Send me the output of these three commands:
git stash show --stat stash@{0}
git stash show --stat stash@{1}
git stash show --stat stash@{4}






















how to get the remote repo url to clone the code using already connected vscode url 

(.venv) PS C:\Users\DELL\OneDrive\Desktop\markwave_live_services> git remote -v
origin  https://github.com/markwaveai/markwave_live_services.git (fetch)
origin  https://github.com/markwaveai/markwave_live_services.git (push)
(.venv) PS C:\Users\DELL\OneDrive\Desktop\markwave_live_services>

"Show me the remote repositories connected to this local Git repository, along with their URLs."



python -m venv .venv 

Quick mental model
Project folder
     │
     └── .venv
          │
          └── Scripts
                └── Activate.ps1
Activate:
.\.venv\Scripts\Activate.ps1
Deactivate:
deactivate




Yes, this command is correct:

pip freeze > requirements.txt

What does it do?

It takes all the Python packages installed in your currently active 
virtual environment and writes them into requirements.txt.

For example, if your .venv contains:
fastapi
uvicorn
neo4j
pydantic
firebase-admin
cryptography

then:

pip freeze > requirements.txt

creates/overwrites:

requirements.txt

with something like:
fastapi==...
uvicorn==...
neo4j==...
pydantic==...
firebase-admin==...
cryptography==...
Important for your project
First activate your .venv:

note : It will overwrite the existing file. It will not create a duplicate.   





(.venv) PS C:\Users\DELL\Downloads\markwave_live_services_Downloads> python -m uvicorn app:app --port 8001



If you wanted to add to the existing file instead, PowerShell uses:

pip freeze >> requirements.txt

Here:

> → overwrite
>> → append to existing file

For requirements.txt, normally you want:

pip freeze > requirements.txt

Yes, you can run multiple FastAPI projects on the same computer,
 including one from VS Code and another from Antigravity.

But you cannot run two servers on the same IP + port combination.

Your error is:
[Errno 10048] error while attempting to bind on address
('127.0.0.1', 8000)

This means:
Port 8000 is already being used by another process.


INFO:     127.0.0.1:61363 - "GET /docs HTTP/1.1" 401 Unauthorized
INFO:     127.0.0.1:62254 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:62254 - "GET /openapi.json HTTP/1.1" 200 OK



Set | = combine two sets and keep unique values.    
 For integers, | means bitwise OR, which is a different concept.  
Example:
{1, 2, 3} | {3, 4, 5}
Result:
{1, 2, 3, 4, 5}




6. Interview answer
If interviewer asks:
"What is Periskope?"
You can say:
"Periskope is a WhatsApp business communication management platform. It provides a shared inbox where multiple team members can manage WhatsApp conversations, assign chats, create tickets, track responses and automate workflows. It is useful when a company has many WhatsApp conversations, numbers, groups or employees and needs centralized visibility and accountability."
"Why do we need it?"
"Normal WhatsApp is mainly designed for communication, whereas businesses need team-level features such as ownership, assignment, conversation history, ticketing, analytics and automation. Periskope provides those capabilities around WhatsApp."
"What happens without it?"
"As the team grows, messages can be missed, multiple employees may respond to the same customer, ownership becomes unclear, managers have limited visibility, and handovers become difficult."
🧠 One-minute memory trick
Remember S-S-G:
Letter	Use case	Problem
S	Sales	Who is handling the customer?
S	Support	Who will resolve the problem?
G	Groups	How do we manage hundreds of conversations?



WITH lets you calculate something once, give it a name, 
and carry that named result into the next stage.

WITH = calculate once → give a name → reuse it in the next stage.   

See the difference
❌ Without WITH
MATCH (p:Person)
WHERE p.age + 10 > 30
RETURN p.name, p.age, p.age + 10 AS future_age


Calculation:
p.age + 10  ← written here
p.age + 10  ← written again


✅ With WITH


MATCH (p:Person)
WITH p.name AS name,
     p.age AS current_age,
     p.age + 10 AS future_age
WHERE future_age > 30
RETURN name, current_age, future_age


usecaselesss using the only return statement : 


give that example  : 
(u:User) 
return u.name 


uisikng with  : 
(u:User) 
with u.name as user_name
return user_name 













Your problem is:
"I'm tracing sales_report() → db_sales_report_aggregate() → "
"some helper. I reached a function. Now I want to go back to the exact"
" caller/line from which I came, not see 100 references and manually find it."


The trick: use Alt + Left — not Find All References.

VS Code maintains a navigation history.
For example, you are tracing:

sales_report()
    │
    │ Ctrl + Click
    ↓
db_sales_report_aggregate()
    │
    │ Ctrl + Click
    ↓
_apply_lead_type()
    │
    │ Ctrl + Click
    ↓
some_helper()


Now you are inside:
def some_helper():

You want to go back to exactly where you came from.

Press:
Alt + Left

You go directly to:
_apply_lead_type(
    db_sales_report_aggregate(...)
)

Then:
Alt + Left

You go directly to:
db_sales_report_aggregate(...)
inside sales_report().


Then:

Alt + Left

You go back to the previous location in sales_report().

This is the important difference
Shift + F12
Means:
"Show me EVERYWHERE this function is used."

If there are 100 references → you'll get 100 references.
That's useful when you want to understand all callers.
'
'Alt + Left
Means:
"Take me back to EXACTLY where I was before."
That's what you want while tracing one particular flow.
Even better: use Alt + Right
Suppose:
sales_report
   ↓
db_sales_report_aggregate
   ↓
helper
You press:

Alt + Left
and go:
helper
   ↑
db_sales_report_aggregate


Then accidentally went too far back.
Press:

Alt + Right
and VS Code moves forward again.
So:
Alt + Left   = Back
Alt + Right  = Forward




When tracing a backend API, don't try to understand every helper function first.'
' First understand the API's business functionality and main flow, then trace helpers only when 
the main flow reaches them.



Think of it like this:
1. What does this API do?
        ↓
2. What comes into the API?
        ↓
3. What should it return?
        ↓
4. What is the main flow?
        ↓
5. Which helper functions are called?
        ↓
6. Only then understand those helpers



Continue   

⚠️ Gemini Code Assist   

🟢 1. GitHub Copilot Free — easiest option  



Health insurance = "What if I get hospitalized?"
Term insurance = "What if I die and my family loses my income?"
Life insurance = broader category of insurance covering human life; term insurance is one type.
========================================================================>
removed 



2. People confuse "I recognize it" with "I can recall it"

This is one of the biggest problems.

You read your notes:
"FastAPI uses dependency injection through Depends()."

You think:
"Yeah, I know this."

But during an interview:

Interviewer: "Why did you use Depends(get_verified_mobile) here?"

Suddenly:
Brain: ..............




The configuration is stored in a singleton Neo4j node:   

singleton measn what  here 
Here, singleton simply means:

There should be only ONE configuration node for the entire application.

In your code:
MATCH (c:MarketingOnboardConfig {id: $id})

The id is used to identify that one configuration node.

Think of a real-world example

Imagine your company has one main office notice board:
Company
   ↓
Main Notice Board
   ↓
Marketing onboarding settings


before creating the branch we should always do the following steps to avoid any conflicts with the main branch :
we should ask from which branch to take the latest pull becaz in that branch only this branch is going to be pushed 
Get latest main → create new branch from latest main → work on it → push it to GitHub 

Complete sequence
If you're currently on main and have no uncommitted changes, the whole process is:
git switch main or staging_live
git pull origin main or staging_live 
git switch -c new_due_payout_deatls
# Make your code changes
git status
git add .
git commit -m "Add new due payout details"
git push -u origin new_due_payout_deatls


how to revert the new changes in the antigravity or else github copilot : 
stop and reverest the changes and 1st delete that chat using the rvert that symbol 

tell chatbot to add a single hi line in the file and delete that chat now observer wheather is it working or not 

how to dlete a brach   :
git branch -d due_payout_details 




One important thing to understand

The word assert means:
"I expect this condition to be true."

The assert keyword is used to check whether something is true.
In simple words:
assert = "I expect this to be true. If it is not true, tell me the test failed."
Simple example
x = 10
assert x == 10
Here Python checks:
Is x equal to 10?
       ↓
      YES ✅
       ↓
Continue
Nothing happens because the condition is true.
But:
x = 10
assert x == 20
Python checks:
Is x equal to 20?
       ↓
       NO ❌
       ↓
AssertionError
So assert is mainly useful for checking assumptions and testing code.
Why was assert introduced?
The main idea is to catch problems automatically instead of manually checking every result.
For example, without assert:
result = add(10, 20)
print(result)
You have to look at the output and decide:
30
Is that correct? You manually check it.
With assert:
result = add(10, 20)
assert result == 30
Now Python automatically checks it.
result = 30
       ↓
30 == 30
       ↓
   True ✅
       ↓
 Test passes
If your function accidentally returns 40:
result = 40
       ↓
40 == 30
       ↓
   False ❌
       ↓
AssertionError




10. Your interview answer
If interviewer asks:
Q: How do you identify which API a frontend application is calling?
You can say:
"For a web application, I open Chrome DevTools and go to the Network tab. When I perform the action in the UI, I can see the HTTP request, including the URL, method, request payload, headers, status code, and response. The API does not need to be explicitly configured to appear in the Network tab; the browser automatically records network requests made by the application."
That's a strong interview answer.
Q: Does the developer explicitly tell Chrome to display the API in Network?
Answer:
"No. The frontend code makes the HTTP request using mechanisms such as fetch or Axios. Chrome DevTools automatically captures and displays those network requests when the Network tab is open."
Q: How do you debug an API issue coming from a mobile application?
Answer:
"First, I identify which API the mobile application is calling, using application logs, network inspection tools, or information from the mobile team. Then I check the API request, status code, backend logs, and trace the corresponding endpoint and service logic in the backend. Finally, I check the database queries and identify where the error occurs."
Q: How do you trace a frontend issue to the backend?
Remember this simple flow:
UI action
   ↓
API request
   ↓
Endpoint
   ↓
Backend function
   ↓
Business logic
   ↓
Database
   ↓
Response
   ↓
UI



Assertion అంటే Telugu లో “దృఢమైన ప్రకటన”, “నిశ్చయంగా చెప్పడం”, లేదా “వాదన/ప్రకటన” అని అర్థం.
Simple meaning:
Assertion = ఒక విషయం నిజమని గట్టిగా చెప్పడం
Example:
He made an assertion that he was innocent.
→ తాను నిర్దోషినని అతను గట్టిగా చెప్పాడు.
Programming లో:
Python లో assertion అంటే ఒక condition నిజమా కాదా అని check చేయడం.



10. Your interview answer
If interviewer asks:
Q: How do you identify which API a frontend application is calling?
You can say:
"For a web application, I open Chrome DevTools and go to the Network tab."
" When I perform the action in the UI, I can see the HTTP request, including the URL, method, request payload,"
" headers, status code, and response. The API does not need to be explicitly configured to appear in the Network tab; "
"the browser automatically records network requests made by the application."


That's a strong interview answer.
'
'Q: Does the developer explicitly tell Chrome to display the API in Network?
Answer:
"No. The frontend code makes the HTTP request using mechanisms such as fetch or Axios. 
Chrome DevTools automatically captures and displays those network requests when the Network tab is open.



why the functins are created than  writtten the alreayd written code a lot times 
=> 


leetcode 
ml 
reactjs file reading 
flutter leactures 
js content taking 
fast api intterview questions in youtube and contentn prepararion 
fast crud apis writting 
neo4j queries writting  


only open the app whe you do have the work over there complete that work come to work bush 

we are employees with zero salries of youtube , whatsapp , facebook , insta , twitter ex : potographers . editors etc.  adn making them rich 

we are 

tricks :

turnoff notificatiosns :
when we to go there then we should go we should not go if someone is calling us 

distance : hide app in another folders 

reminders to stop the application 

using the 3 accounts for each purpose to give the goood feed to it 

passion 
obsession 
addition 

🔴 3. Addiction   : 
"I don't want to do it, but I feel unable to stop."   

⚡ 2. Obsession
Obsession = "I keep thinking about it."
You may still have some control, but the activity starts occupying your mind excessively. 

🔥 1. Passion
Passion = "I really want to do this."
Then you stop and go to sleep.
I WANT TO DO IT
       ↓
I DO IT
       ↓
I CAN STOP
That's passion.




For a Flutter application, there is no browser Network tab by default, 
but Flutter developers have several ways to trace the API calls.

 1. The easiest way: Flutter/Android Studio logs
If the Flutter app uses packages such as dio or http, developers commonly add request/response logging.
For example, with Dio:

final dio = Dio();
dio.interceptors.add(
  LogInterceptor(
    request: true,
    requestHeader: true,
    requestBody: true,
    responseBody: true,
    responseHeader: true,
    error: true,
  ),
);

Then when you perform an action in the app, the console may show:

REQUEST:

POST https://api.example.com/api/orders

Request Body:
{
  "product_id": 123,
  "quantity": 2
}

RESPONSE:
200

Response:
{
  "status": "success",
  "order_id": 456
}
So you immediately know:
Flutter Action
     ↓
Dio request
     ↓
POST /api/orders
     ↓
Backend
     ↓
Response

3. Flutter DevTools
Flutter also has Dart DevTools, which is useful for debugging the application.
You can inspect things such as:
 logs 
 exceptions 
 performance 
 network-related information depending on the setup 
 application behavior 
However, in day-to-day API debugging, HTTP logging/interceptors are often much simpler.






Encoding = converting information FROM its original form INTO another representation.
Decoding = converting that representation BACK into a usable/original form. 

Encoding = Pack the information 📦
Decoding = Unpack the information 📦 → 📄

1. Simple real-life example 🗣️

Suppose I have:
"HELLO"

I convert it into numbers:
H → 8
E → 5
L → 12
L → 12
O → 15
So:

HELLO
  ↓
8 5 12 12 15

This conversion is encoding.

Now suppose I receive:

8 5 12 12 15

I convert it back:
8 → H
5 → E
12 → L
12 → L
15 → O
This is decoding.

So:
Original information
        ↓
     ENCODING
        ↓
Different representation
        ↓
     DECODING
        ↓
Original information


So if interviewer asks:
"Why AES-GCM instead of AES-CBC?"
You can say:
"AES-CBC provides confidentiality,"
" but it does not inherently provide authentication. "
"AES-GCM provides authenticated encryption, meaning it protects the confidentiality"
" of the data and also detects tampering. That makes AES-GCM a convenient and robust"
" choice for protecting API data." 


Think:

AES = lock 🔐
 GCM = tamper detector 🛡️

 AES-GCM = locked box + tamper detection 
AES-GCM stands for Advanced Encryption Standard - Galois/Counter Mode   

🆚 AES-GCM vs AES-CBC — easy interview comparison

Feature

AES-CBC
AES-GCM

Encryption
✅
✅

Detects tampering by itself
❌
✅

Authentication tag
❌
✅

Good modern API choice

Requires extra authentication design

✅ Common choice

Performance
Good
Very good, especially with hardware support
Implementation complexity
More components needed for authenticated encryption

Simpler authenticated-encryption API

🔑 One very important thing: the nonce

Since you've been working with AES-GCM, you should know this interview point.

AES-GCM uses a nonce (also called an IV).


Typically:

AES-GCM
   +
Secret Key
   +
Nonce
   +
Plaintext
   ↓
Ciphertext + Authentication Tag

For AES-GCM, the nonce must never be reused with the same key.

A common practice is to generate a fresh 12-byte nonce for each encryption.




| Term           | Simple meaning                                           | Intuition                           | Example                     |
| -------------- | -------------------------------------------------------- | ----------------------------------- | --------------------------- |
| **Encoding**   | Change data into another format                          | 📦 **Pack it in a standard format** | `Hello → SGVsbG8=` (Base64) |
| **Decoding**   | Convert encoded data back                                | 📦 **Unpack the standard format**   | `SGVsbG8= → Hello`          |
| **Encryption** | Change data so others cannot understand it without a key | 🔐 **Lock it with a key**           | `Hello → x7$K@92#`          |
| **Decryption** | Use the key to turn encrypted data back                  | 🔑 **Unlock it with the key**       | `x7$K@92# → Hello`          |




A coupon code is a special code that gives you a discount or special benefit when you buy something.

Simple real-life example 🛒

Suppose you go to an online shopping website.

You want to buy a shirt:

Shirt price = ₹1,000

At checkout, you see:

Coupon Code: SAVE100
You enter:
SAVE100
The website says:
Original price = ₹1,000
Discount     = ₹100
--------------------
You pay      = ₹900

So, SAVE100 is the coupon code.


Why are coupon codes introduced?

Companies introduce coupon codes mainly to encourage customers to buy.
For example:
Imagine an online store has a new customer.

The company says:
"If you make your first purchase, use WELCOME10 and get 10% off."
Customer sees:

Product = ₹2,000
WELCOME10
    ↓
10% discount
    ↓
₹200 discount
Final price = ₹1,800

The customer saves ₹200, and the company gets a new customer.





========================================================================>
daily tasks and task numbers(task_ids) : 

farm apis 
visit location apis 
users apis 
products apis 


07-09-2026 :
1881

08-09-2026 :
1882 

15-09-2026 tues  
1910

16-09-2026 tues  
1912

17-09-2026 tues  
1913

18-09-2026 tues  
1929

19-09-2026 tues  


21-09-2026 mon
1846 
1907 

22-09-2026 tues  
1930
1926


23-09-2026 wed  
1954
1955

24-09-2026 thur  
2017
2018

25-09-2026 fri  
2026 => traced the all leads apis 

26-09-2026 sat  
2039 ==> 1st 8 apis traced in that marketing module 

27-09-2026 sun  
1930
1926

28-09-2026 mon  
1930
1926

29-09-2026 tues  
1930
1926

30-09-2026 wed  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926

22-09-2026 tues  
1930
1926


========================================================================>

@router.get(
    "/due-details",
    summary="List orders by payout due date",
    description=(
        "Return paid orders whose first payout due date falls within "
        "the requested payout date range. The first payout date is "
        "calculated as 61 days after SuperAdmin approval."
    ),
)
async def list_payout_due_orders(
    x_admin_mobile: Optional[str] = Header(None),

    verified_mobile: Optional[str] = Depends(get_verified_mobile),

    search: Optional[str] = Query(
        None,
        description="Search by Order ID, User Mobile, or User Name",
    ),

    farmId: Optional[str] = Query(
        None,
        description="Filter by Farm ID",
    ),

    from_date: Optional[str] = Query(
        None,
        description="Payout due date from (YYYY-MM-DD), inclusive",
    ),

    end_date: Optional[str] = Query(
        None,
        description="Payout due date to (YYYY-MM-DD), inclusive",
    ),

    onboardedByMobile: Optional[str] = Query(
        None,
        description="Filter by marketing executive mobile",
    ),

    page: int = Query(1, ge=1),

    page_size: int = Query(10, ge=1, le=100000),
) -> Dict[str, Any]:
    x_admin_mobile = resolve_caller_mobile(x_admin_mobile, verified_mobile)

    try:
        # Normalize caller mobile (header may carry stray whitespace)
        x_admin_mobile = (x_admin_mobile or "").strip()

        driver = get_shared_driver()
        try:
            with driver.session() as session:

                skip = (page - 1) * page_size
                # Resolve caller role
                role_rec = session.run(
                    "MATCH (u:User {mobile: $mobile}) RETURN u.role AS role",
                    mobile=x_admin_mobile,
                ).single()

                if not role_rec:
                    return {"statuscode": 403, "status": "error", "message": "Unauthorized: User not found"}

                role_parts = {r.strip() for r in (role_rec["role"] or "").split(",") if r.strip()}
                if not role_parts.intersection(DASHBOARD_STAFF_ROLES):
                    return {"statuscode": 403, "status": "error", "message": "Dashboard staff access required"}
                # 🔹 Order-level filters
                # Soft-deleted orders must never surface in the admin dashboard.
                # order_conditions = ["u.paymentStatus IN $statuses", "coalesce(u.status,'') <> 'DELETED'"]
                order_conditions = [
                    "coalesce(u.status, '') <> 'DELETED'",
                    "u.paymentStatus = 'PAID'",
                    "u.adminApprovedAt IS NOT NULL",
                    "u.superAdminApprovedAt IS NOT NULL",
                ]
                # Search matches (case-insensitive, partial) across: Order ID, buyer
                # phone (userId), buyer name (name / first / last / full name), and the
                # referrer's phone + name. `ref` is OPTIONAL-MATCHed before the WHERE in
                # every query below so it is in scope here.
                search_predicate = (
                    "(toLower(u.id) CONTAINS toLower($search) "
                    "OR u.userId CONTAINS $search "
                    "OR toLower(coalesce(i.name, '')) CONTAINS toLower($search) "
                    "OR toLower(coalesce(i.first_name, '')) CONTAINS toLower($search) "
                    "OR toLower(coalesce(i.last_name, '')) CONTAINS toLower($search) "
                    "OR toLower(trim(coalesce(i.first_name, '') + ' ' + coalesce(i.last_name, ''))) CONTAINS toLower($search) "
                    "OR coalesce(toString(ref.mobile), '') CONTAINS $search "
                    "OR toLower(coalesce(ref.name, '')) CONTAINS toLower($search) "
                    "OR toLower(coalesce(ref.first_name, '')) CONTAINS toLower($search) "
                    "OR toLower(coalesce(ref.last_name, '')) CONTAINS toLower($search) "
                    "OR toLower(trim(coalesce(ref.first_name, '') + ' ' + coalesce(ref.last_name, ''))) CONTAINS toLower($search))"
                )

                if search:
                    order_conditions.append(search_predicate)

                # Convert the user's requested payout-date range
                # into the corresponding SuperAdmin approval-date range.

                # Business rule:
                # first_due_date = superAdminApprovedAt + 61 days
                # Therefore:
                # superAdminApprovedAt = first_due_date - 61 days

                payout_from_date = None
                payout_end_date = None

                if from_date:
                    payout_from_date = (
                        datetime.strptime(from_date, "%Y-%m-%d").date()
                        - timedelta(days=61)
                    ).isoformat()

                if end_date:
                    payout_end_date = (
                        datetime.strptime(end_date, "%Y-%m-%d").date()
                        - timedelta(days=61)
                    ).isoformat()

                if payout_from_date:
                    order_conditions.append(
                        "date(u.approvalDate) >= date($payout_from_date)"
                    )

                if payout_end_date:
                    order_conditions.append(
                        "date(u.approvalDate) <= date($payout_end_date)"
                    )

                if onboardedByMobile:
                    order_conditions.append("u.unit_placed_by_mobile = $onboarded_by_mobile")

                order_where = " AND ".join(order_conditions)

                # 🔹 Farm Logic
                # Orders are already scoped to the caller (orderCreatedByMobile / orderUpdatedByMobile),
                # so the farm relationship is only used for the optional farmId filter and for enrichment.
                if farmId:
                    farm_clause = "MATCH (u)-[:ALLOCATED_TO]->(f:Farm)"
                    farm_where_part = "WHERE f.id = $farmId"
                else:
                    farm_clause = "OPTIONAL MATCH (u)-[:ALLOCATED_TO]->(f:Farm)"
                    farm_where_part = ""

                # 🔹 Main query — group all transactions under each order
                query = f"""
                MATCH (u:AnimalKartOrder)
                OPTIONAL MATCH (i:User {{mobile: u.userId}})
                OPTIONAL MATCH (i)-[:REFERREDBY]->(ref:User)
                WITH u, i, ref
                WHERE {order_where}
                {farm_clause}
                {farm_where_part}
                OPTIONAL MATCH (u)-[:HAS_TRANSACTION]->(t:Transaction)
                OPTIONAL MATCH (u)-[:HAS_INVOICE]->(inv:Invoice)
                WITH u, i, f, inv, ref, collect(t) AS transactions
                ORDER BY coalesce(u.superAdminApprovedAt, u.superAdminRejectedAt, u.adminApprovedAt, u.adminRejectedAt, u.submittedAt, u.placedAt) DESC
                SKIP $skip
                LIMIT $limit
                RETURN u, transactions, i, f, inv, ref
                """

                result = session.run(
                    query,
                    search=search,
                    farmId=farmId,
                    payout_from_date=payout_from_date,
                    payout_end_date=payout_end_date,
                    onboarded_by_mobile=onboardedByMobile,
                    skip=skip,
                    limit=page_size,
                    admin_mobile=x_admin_mobile,
                )

                orders = []
                for record in result:
                    u = dict(record["u"])
                    i = record.get("i")
                    f = record.get("f")
                    inv = record.get("inv")
                    ref = record.get("ref")

                    # Get location from Farm
                    if f:
                        farm_data = dict(f)
                        u["location"] = farm_data.get("location")
                    else:
                        u["location"] = None
                    # 🔹 Referrer (who referred the investor) — via REFERREDBY relationship
                    referred_by = None
                    if ref:
                        ref_node = dict(ref)
                        ref_name = (
                            ref_node.get("name")
                            or f"{ref_node.get('first_name', '') or ''} {ref_node.get('last_name', '') or ''}".strip()
                            or None
                        )
                        ref_mobile = ref_node.get("mobile") or ref_node.get("id")
                        referred_by = {
                            "name": ref_name,
                            "mobile": ref_mobile,
                            "referral_code": ref_node.get("referral_code"),
                        }

                    orders.append(
                        convert_neo4j_datetime({
                            "order": u,
                            "investor": dict(i) if i else None,
                            "referredBy": referred_by,
                        })
                    )

                # Marketing exec who placed each order on the investor's behalf
                # (UNIT_PLACED_BY / o.unit_placed_by_mobile) — only the mobile is
                # stored on the order itself, so resolve names in one batch query.
                onboarded_by_mobiles = {
                    entry["order"].get("unit_placed_by_mobile")
                    for entry in orders if entry["order"].get("unit_placed_by_mobile")
                }
                onboarded_by_map: Dict[str, Dict[str, Any]] = {}
                if onboarded_by_mobiles:
                    for row in session.run(
                        "MATCH (e:User) WHERE e.mobile IN $mobiles "
                        "RETURN e.mobile AS mobile, "
                        "       trim(coalesce(e.first_name,'') + ' ' + coalesce(e.last_name,'')) AS name, "
                        "       e.role AS role",
                        mobiles=list(onboarded_by_mobiles),
                    ).data():
                        onboarded_by_map[row["mobile"]] = {"name": row["name"] or None, "role": row["role"]}
                # Which of each order's units have since been transferred, and
                # to whom — one query for the whole page, like the batch above.
                # Without it this list names the investor as owner of units he
                # no longer holds.
                status_map = db_unit_transfer_status(
                    session,
                    [entry["order"].get("id") for entry in orders
                     if entry["order"].get("id")],
                )

                for entry in orders:
                    status = status_map.get(entry["order"].get("id")) or empty_status()

                    entry["order"]["numUnits"] = status["total_units"]

                    # Business rules:
                    # - First due payout/date are applicable only when:
                    #   1. paymentStatus is PAID
                    #   2. Admin has approved the order
                    #   3. SuperAdmin has approved the order
                    # - Once both approvals are present, use superAdminApprovedAt
                    #   as the approved date.
                    # - First due date = exactly 61 days after SuperAdmin approval.
                    # - If any condition is not satisfied, both fields remain None.
                    total_units = int(status.get("total_units") or 0)

                    payment_status = entry["order"].get("paymentStatus")
                    admin_approved_at = entry["order"].get("adminApprovedAt")
                    super_admin_approved_at = entry["order"].get("superAdminApprovedAt")

                    # Only add first_due_payout and first_due_date
                    # when all required conditions are satisfied.
                    if (
                        payment_status == "PAID"
                        and admin_approved_at
                        and super_admin_approved_at
                    ):
                        try:
                            # Use SuperAdmin approval date
                            approved_at = super_admin_approved_at
                            # First payout = total units × ₹9,000
                            entry["order"]["first_due_payout"] = total_units * 9000

                            if isinstance(approved_at, str):
                                # Neo4j may return nanosecond precision.
                                # Python datetime supports only 6 microsecond digits.
                                approved_at = re.sub(
                                    r"(\.\d{6})\d+",
                                    r"\1",
                                    approved_at
                                )
                                approved_date = datetime.fromisoformat(
                                    approved_at.replace("Z", "+00:00")
                                )
                            else:
                                approved_date = approved_at
                            # First due date = exactly 61 days after
                            # SuperAdmin approval date
                            entry["order"]["first_due_date"] = (
                                approved_date + timedelta(days=61)
                            ).isoformat()

                        except Exception as e:
                            logger.exception(
                                f"[DUE DATE ERROR] Failed to calculate first_due_date: {e}"
                            )
                            # Remove the fields if calculation fails
                            entry["order"].pop("first_due_payout", None)
                            entry["order"].pop("first_due_date", None)
                # 🔹 Filtered count + payout summary
                # The summary is calculated for ALL filtered orders,
                # not only the orders present on the current page.
                # paid_units:
                #     Total units across all filtered PAID orders.
                # total_due_pay_amount:
                #     Total units × ₹9,000.
                
                # paid_due_amount:
                #     Sum of amount_credited from FirstDuePayOut nodes
                #     where is_amount_credited = true.
                
                # pending_due_amount:
                #     Total due amount - already credited amount.

                summary_query = f"""
                MATCH (u:AnimalKartOrder)
                OPTIONAL MATCH (i:User {{mobile: u.userId}})
                OPTIONAL MATCH (i)-[:REFERREDBY]->(ref:User)
                WITH u, i, ref
                WHERE {order_where}
                {farm_clause}
                {farm_where_part}

                OPTIONAL MATCH (u)-[:FirstDuePayOut]->(p:FirstDuePayOut)

                RETURN
                    count(DISTINCT u) AS total_filtered,

                    collect(DISTINCT u.id) AS order_ids,

                    coalesce(
                        sum(
                            CASE
                                WHEN p.is_amount_credited = true
                                THEN coalesce(p.amount_credited, 0)
                                ELSE 0
                            END
                        ),
                        0
                    ) AS paid_due_amount
                """
                summary_record = session.run(
                    summary_query,
                    search=search,
                    farmId=farmId,
                    payout_from_date=payout_from_date,
                    payout_end_date=payout_end_date,
                    onboarded_by_mobile=onboardedByMobile,
                    admin_mobile=x_admin_mobile,
                ).single()

                total_filtered = summary_record["total_filtered"]
                summary_order_ids = summary_record["order_ids"] or []
                paid_due_amount = int(summary_record["paid_due_amount"] or 0)

                # Get the effective unit count for ALL filtered orders.
                # This is the same unit-transfer logic already used by the API.
                summary_status_map = db_unit_transfer_status(
                    session,
                    summary_order_ids,
                )
                paid_units = 0
                total_due_pay_amount = 0

                for order_id in summary_order_ids:
                    status = summary_status_map.get(order_id) or empty_status()

                    total_units = int(status.get("total_units") or 0)

                    paid_units += total_units
                    total_due_pay_amount += total_units * 9000

                # Amount that is still pending to be paid.
                pending_due_amount = max(
                    total_due_pay_amount - paid_due_amount,
                    0,
                )

                # 🔹 Final response
                response_orders = []

                for entry in orders:
                    order = entry["order"]
                    investor = entry["investor"]

                    response_order = {
                        "id": order.get("id"),
                        "approvalDate": order.get("approvalDate"),
                        "numunits": order.get("numUnits"),
                        "paymentstatus": order.get("paymentStatus"),
                        "user_id": order.get("user_id"),
                        "location": order.get("location"),
                    }

                    if "first_due_payout" in order:
                        response_order["first_due_payout"] = order["first_due_payout"]

                    if "first_due_date" in order:
                        response_order["first_due_date"] = order["first_due_date"]

                    response_orders.append({
                        "order": response_order,
                        "investor": {
                            "name": f"{investor.get('first_name', '')} {investor.get('last_name', '')}".strip() if investor else None,
                            "mobile": investor.get("mobile") if investor else None,
                        },
                        "referredBy": entry.get("referredBy"),
                    })

                return {
                    "statuscode": 200,
                    "status": "success",
                    "page": page,
                    "page_size": page_size,
                    "total_filtered": total_filtered,
                    "paid_units": paid_units,
                    "total_due_pay_amount": total_due_pay_amount,
                    "paid_due_amount": paid_due_amount,
                    "pending_due_amount": pending_due_amount,
                    "orders": response_orders,
                }
        finally:
            pass 
    except Exception as e:
        return {
            "statuscode": 500,
            "status": "error",
            "message": str(e),
        }

========================================================================>
The endpoint handling the request is list_marketing_orders in routers/marketing.py.

The onboardedByMobile query parameter is captured by MarketingOrderFilters.

It is passed down to db_marketing_orders (and the related count / stats helpers)
 where the Cypher query adds a condition o.unit_placed_by_mobile = $onboarded_by_mobile.

The filter works on the unit_placed_by_mobile property of the AnimalKartOrder node,
 not on a relationship node directly, and is constrained by the caller’s overall visibility scope.



========================================================================>

def db_marketing_orders(session, exec_mobiles: List[str],
                        paid_only: bool = False,
                        unapproved_only: bool = False,
                        with_cache: bool = False,
                        payment_status: Optional[str] = None,
                        search: Optional[str] = None,
                        from_date: Optional[str] = None,
                        end_date: Optional[str] = None,
                        with_cpf: Optional[bool] = None,
                        onboarded_by_mobile: Optional[str] = None,
                        skip: Optional[int] = None,
                        limit: Optional[int] = None):
    """Unit orders placed by any of the given executives.

    `skip`/`limit` page the result. Both omitted returns every matching order,
    which is what the aggregating callers (the leaderboard, the pending queue)
    still want.

    `with_cache=True` returns (rows, cache) instead of rows, so a caller that
    aggregates over the incentives can reuse the plan and units-so-far already
    fetched for the per-order projections rather than querying them again.
    """
    where, search_clause, params = _marketing_orders_filter(
        exec_mobiles, paid_only=paid_only, unapproved_only=unapproved_only,
        payment_status=payment_status, search=search, from_date=from_date,
        end_date=end_date, with_cpf=with_cpf,
        onboarded_by_mobile=onboarded_by_mobile)

    # Paged in Cypher, not in Python: slicing after the fact would still build
    # every row's transaction and unit collections, and then run the per-order
    # incentive projection over all of them.
    page_clause = ""
    if limit is not None:
        params["skip"] = int(skip or 0)
        params["limit"] = int(limit)
        page_clause = " SKIP $skip LIMIT $limit"

    rows = [dict(r) for r in session.run(
        _ORDERS_MATCH.format(where=where) +
        f"{search_clause}"
        # Marketing creates the order; an EMPLOYEE attaches the payments. The
        # Manager needs to see how the money arrived before approving, so the
        # transactions come back with the order rather than needing a second call.
        # `lead` is carried the whole way down for the lead_name/lead_mobile_number
        # columns — it used to be dropped here, which is why the listing could
        # search by lead but never show one.
        # Who referred the INVESTOR — the peer REFERREDBY edge, not the marketing
        # onboarding edge. It is what makes an order DIRECT or INDIRECT, so a
        # manager approving the incentive should be able to see it next to the
        # amount. head(collect(...)) rather than a plain OPTIONAL MATCH because a
        # second REFERREDBY edge would otherwise duplicate the order row.
        "WITH o, r, e, i, lead "
        "OPTIONAL MATCH (i)-[:REFERREDBY]->(refu:User) "
        "WITH o, r, e, i, lead, head(collect(refu)) AS ref "
        "OPTIONAL MATCH (o)-[:HAS_TRANSACTION]->(t:Transaction) "
        "WITH o, r, e, i, lead, ref, t ORDER BY t.createdAt DESC "
        "WITH o, r, e, i, lead, ref, "
        "     collect(CASE WHEN t IS NULL THEN null ELSE { "
        "         id: t.id, "
        "         amount: coalesce(t.amount, 0), "
        "         paymentMethod: coalesce(t.paymentMethod, ''), "
        "         status: coalesce(t.status, ''), "
        "         utrNumber: coalesce(t.utrNumber, ''), "
        "         transferMode: coalesce(t.transferMode, ''), "
        # toString() because createdAt is a neo4j DateTime, which FastAPI's JSON
        # encoder cannot serialise.
        "         transactionDate: toString(coalesce(t.transactionDate, '')), "
        "         createdAt: toString(coalesce(t.createdAt, '')), "
        "         recorded_by_mobile: coalesce(t.paymentUpdatedByMobile, ''), "
        "         recorded_by_name: coalesce(t.paymentUpdatedByName, ''), "
        "         recorded_by_role: coalesce(t.paymentUpdatedByRole, '') "
        "     } END) AS all_txns, "
        # SURPLUS is an over-payment credited to the money wallet, excluded from
        # coverage everywhere else in purchases.py — keep totalPaid consistent.
        "     sum(CASE WHEN t IS NULL OR coalesce(t.paymentMethod,'') = 'SURPLUS' "
        "              THEN 0 ELSE coalesce(t.amount, 0) END) AS totalPaid "
        " OPTIONAL MATCH (o)-[:HAS_UNIT]->(u:Unit) "
        " OPTIONAL MATCH (u)-[:HAS_NOMINEE]->(n:Nominee) "
        " WITH o, r, e, i, lead, ref, all_txns, totalPaid, u, n ORDER BY u.unitIndex "
        " WITH o, r, e, i, lead, ref, all_txns, totalPaid, "
        "     collect(CASE WHEN u IS NULL THEN null ELSE { "
        "         unit_id: u.id, "
        "         unit_index: u.unitIndex, "
        "         breed_id: u.breedId, "
        "         nominee: CASE WHEN n IS NULL THEN null ELSE n { .*, createdAt: toString(n.createdAt) } END "
        "     } END) AS all_units "
        "RETURN o.id AS order_id, o.userId AS investor_mobile, "
        "       trim(coalesce(i.first_name,'') + ' ' + coalesce(i.last_name,'')) AS investor_name, "
        "       o.numUnits AS numUnits, "
        "       coalesce(o.paymentStatus, '') AS paymentStatus, "
        "       coalesce(o.status, '') AS status, "
        "       coalesce(o.totalCost, 0) AS totalCost, "
        "       totalPaid, "
        "       coalesce(o.withCpf, false) AS with_cpf, "
        "       [x IN all_txns WHERE x IS NOT NULL] AS transactions, "
        "       [x IN all_units WHERE x IS NOT NULL] AS units, "
        "       coalesce(o.lead_id, '') AS lead_id, "
        "       coalesce(lead.full_name, '') AS lead_name, "
        # The lead's own number, which is often not the investor's: a lead is
        # captured before anyone signs up, so this is the number marketing
        # actually called.
        "       coalesce(toString(lead.mobile_number), toString(lead.phone_number), '') AS lead_mobile_number, "
        # Where the lead came from. `platform` is the ad platform or the chosen
        # source; `campaign_name` names the specific ad it answered, which is
        # what "which campaign is this sale from" actually asks. reference_*
        # only exist on a Reference lead — the person who passed the name on.
        "       coalesce(lead.platform, '') AS lead_platform, "
        "       coalesce(lead.campaign_name, '') AS lead_campaign_name, "
        "       coalesce(lead.lead_status, '') AS lead_status, "
        "       coalesce(lead.reference_name, '') AS lead_reference_name, "
        "       coalesce(toString(lead.reference_number), '') AS lead_reference_number, "
        # The investor's referrer, resolved above.
        "       coalesce(ref.mobile, '') AS referred_by_mobile, "
        "       trim(coalesce(ref.first_name,'') + ' ' + coalesce(ref.last_name,'')) AS referred_by_name, "
        "       coalesce(ref.user_id, '') AS referred_by_user_id, "
        "       coalesce(ref.role, '') AS referred_by_role, "
        "       coalesce(o.incentive_approved, false) AS incentive_approved, "
        "       coalesce(o.incentive_approved_by, '') AS incentive_approved_by, "
        "       toString(coalesce(o.incentive_approved_at, '')) AS incentive_approved_at, "
        "       e.mobile AS unit_placed_by_mobile, "
        "       toString(coalesce(r.placed_at, '')) AS placed_at "
        "ORDER BY r.placed_at DESC" + page_clause,
        **params)]

    approvers = db_approver_names(session, (r.get("incentive_approved_by") for r in rows))

    cache: dict = {}
    for row in rows:
        # Who signed the incentive off, by name. Falls back to the bare mobile
        # rather than a blank: an approval with an unresolvable approver still
        # happened, and hiding that would read as "never approved".
        approver = approvers.get(normalize_mobile(row.get("incentive_approved_by") or ""), {})
        row["incentive_approved_by_name"] = approver.get("name", "")
        row["incentive_approved_by_role"] = approver.get("role", "")
        credit = db_order_credit_target(session, row["investor_mobile"], row["order_id"])
        row["lead_type"] = credit["source_type"] if credit else ""
        # Display label for the raw stored platform ('ig' -> 'Instagram'); the
        # raw value stays on the row so a consumer can still filter on it.
        row["lead_source"] = lead_source_label(row.get("lead_platform"))
        row["cpf_status"] = cpf_status_label(row.get("with_cpf"))
        # What this order pays, and why — CREDITED once approved, PROJECTED
        # once paid, PENDING before that. Reuses the credit target already
        # resolved above rather than looking the exec up a second time.
        row["incentive"] = order_incentive(session, row, credit, cache)
    return (rows, cache) if with_cache else rows

========================================================================>

how many days will take to create the new obc certificateIn Andhra Pradesh, obtaining a new Central OBC-NCL certificate through a Grama Sachivalayam or MeeSeva centre typically takes 7 to 15 days.The exact timeline depends on whether you already hold a valid, digitally signed permanent state BC caste certificate:⚡ Fast-Track Method (7 Days): If you already have your permanent MeeSeva state BC certificate, the digital verification process is much quicker. The Sachivalayam operator simply uses your existing caste application data and links your current family income documents to issue the central format certificate. Under the official MeeSeva Service Level Agreement (SLA), this is classified as a "Category B" service and is legally mandated to be processed within 7 working days.⏳ Standard Method (15 Days): If you are applying for both a fresh caste validation and an OBC-NCL certificate simultaneously, the application must pass down to the local VRO (Village Revenue Officer) and Panchayat Secretary for local field verification. Once verified, it goes up to the Tahsildar for final approval, taking up to 15 days total.Pro Tips to Speed Up the Process:Apply Proactively: Do not wait for the formal GDS merit list selection message or physical call letter. Walk into your local Sachivalayam tomorrow morning to submit your details.Track Online: You can continuously track the daily live status of your file using your transaction number directly on the AP MeeSeva Application Tracker.Do you currently hold an active, digital MeeSeva State BC Certificate or a current Income Certificate from your local secretariat? Knowing this will help determine if you qualify for the faster 7-day turnaround window.
========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>


========================================================================>