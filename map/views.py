from django.shortcuts import render
from userauths.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.http import JsonResponse
from collections import defaultdict
from plofile.models import Disease
from django.utils.timezone import localtime
# Create your views here.

@login_required(login_url='userauths:sign-in')
def index_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/index-map.html",context)

@login_required(login_url='userauths:sign-in')
def heat_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/heat-map.html",context)

@login_required(login_url='userauths:sign-in')
def cluster_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/cluster-map.html",context)

@login_required(login_url='userauths:sign-in')
def env_map(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/env-map.html",context)

@login_required(login_url='userauths:sign-in')
def analyze(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request,"map/analyze.html",context)




STATE_CITY_MAP = {
    'Andaman & Nicobar Islands': ['Nicobars', 'South Andamans'],
    'Andhra Pradesh': ['Nandamuri Taraka Rama Rao (NTR)', 'Y.S.R.', 'Bapatla', 'Tirupati',
            'Palnadu', 'Sri Sathya Sai', 'Nandyal', 'Anantapur', 'Chittoor',
            'SPSR Nellore', 'Kurnool', 'NTR', 'Alluri Sitharama Raju',
            'Annamayya', 'Kakinada', 'Krishna', 'Prakasam', 'Srikakulam',
            'Anakapalli', 'Visakhapatanam', 'Vizianagaram',
            'Y. S. Rajasekhara Reddy',
            'Y.S.R. (Yeduguri Sandinti Rajasekhara Reddy)'],
    'Arunachal Pradesh': ['East Kameng', 'Upper Subansiri', 'Papumpare', 'Longding',
            'Papum Pare', 'Tawang', 'Leparada', 'Lohit', 'Namsai',
            'West Kameng', 'West Siang'],
    'Assam': ['Charaideo', 'Darrang', 'Hojai', 'Sonitpur', 'Lakhimpur',
            'Dhemaji', 'Bongaigaon', 'Goalpara', 'Udalguri', 'Jorhat',
            'Biswanath', 'Dhubri', 'Dibrugarh', 'Sivasagar', 'Kamrup',
            'Karbi Anglong', 'Kokrajhar', 'Majuli', 'Marigaon', 'Nagaon',
            'Tinsukia', 'Bajali', 'Karimganj', 'Cachar', 'Golaghat',
            'South Salmara Mancachar', 'Nalbari', 'Kamrup Metro', 'Chirang',
            'Barpeta', 'Hailakandi'],
    'Bihar': ['Jehanabad', 'Pashchim Champaran', 'Begusarai', 'Madhubani',
            'Purbi Champaran', 'Arwal', 'Samastipur', 'Bhojpur', 'Saharsa',
            'Sheohar', 'Vaishali', 'Gaya', 'Khagaria', 'Patna', 'Kishanganj',
            'Madhepura', 'Gopalganj', 'Jamui', 'Aurangabad', 'Saran',
            'Katihar', 'Buxar'],
    'Chhattisgarh': ['Raigarh', 'Bijapur', 'Gariyaband', 'Sukma', 'Bemetara',
            'Rajnandgaon', 'Bilaspur', 'Durg', 'Raipur', 'Janjgir-Champa',
            'Sarangarh Bilaigarh', 'Baloda Bazar', 'Kabirdham', 'Mahasamund',
            'Sakti', 'Surajpur', 'Balod', 'Surguja', 'Bastar', 'Dhamtari',
            'Mungeli', 'Jashpur', 'Kanker'],
    'D&N Haveli And Daman And Diu': ['Daman'],
    'Dadra And Nagar Haveli And Daman And Diu': ['Dadra And Nagar Haveli'],
    'Goa': ['North Goa', 'South Goa'],
    'Gujarat': ['Ahmedabad', 'Surendranagar', 'Amreli', 'Morbi', 'Gandhinagar',
            'Valsad', 'Anand', 'Vadodara', 'Jamnagar', 'Gir Somnath',
            'Junagadh', 'Arvalli', 'Bharuch', 'Kheda', 'Devbhumi Dwarka',
            'Rajkot', 'Chhotaudepur', 'Surat', 'Navsari', 'Patan',
            'Panchmahals', 'Sabar Kantha', 'Botad', 'Kachchh', 'Bhavnagar',
            'Ahmadabad', 'Mahisagar', 'Narmada', 'Dohad', 'Mahesana',
            'Sabarkantha'],
    'Haryana': ['Nuh', 'Fatehabad', 'Panchkula', 'Karnal', 'Yamunanagar',
            'Kurukshetra'],
    'Himachal Pradesh': ['Mandi', 'Hamirpur', 'Kangra', 'Kinnaur'],
    'Jammu and Kashmir': ['Badgam', 'Anantnag', 'Shopian', 'Pulwama', 'Jammu', 'Kathua',
            'Baramulla', 'Ganderbal', 'Kupwara', 'Rajauri', 'Doda', 'Srinagar',
            'Bandipora', 'Samba', 'Udhampur', 'Poonch', 'Ramban', 'Reasi',
            'Kulgam'],
    'Jharkhand': ['East Singhbum', 'Simdega', 'Khunti', 'Dumka', 'West Singhbhum',
            'Chatra', 'Deoghar', 'Garhwa', 'Jamtara', 'Giridih',
            'Saraikela Kharsawan', 'Godda', 'Hazaribagh', 'Gumla', 'Koderma',
            'Lohardaga', 'Ranchi', 'Dhanbad', 'Pakur', 'Latehar', 'Sahebganj',
            'Bokaro'],
    'Karnataka': ['Shivamogga', 'Vijayanagar', 'Belagavi', 'Chamarajanagar',
            'Chitradurga', 'Uttar Kannad', 'Haveri', 'Raichur',
            'Chikkamagaluru', 'Dakshin Kannad', 'Koppal', 'Tumakuru',
            'Bagalkot', 'Udupi', 'Vijayapura', 'Chikballapur', 'Gadag',
            'Bengaluru Urban', 'Ballari', 'Hassan', 'Kodagu', 'Mysuru',
            'Ramanagara', 'Bengaluru Rural', 'Bidar', 'Mandya', 'Kolar',
            'Kalaburagi', 'Yadgir', 'Davangere', 'Dharwad'],
    'Kerala': ['Palakkad', 'Thrissur', 'Alappuzha', 'Kannur', 'Kasaragod',
            'Thiruvananthapuram', 'Kottayam', 'Wayanad', 'Ernakulam',
            'Kozhikode', 'Malappuram', 'Kollam', 'Idukki', 'Pathanamthitta'],
       
    'Ladakh': ['Leh Ladakh'],
    'Madhya Pradesh': ['Barwani', 'Chhatarpur', 'Chhindwara', 'Narsinghpur', 'Dhar',
            'Guna', 'Bhopal', 'Burhanpur', 'Gwalior', 'Sheopur', 'Shivpuri',
            'Rewa', 'Alirajpur', 'Betul', 'Mandla', 'Jhabua', 'Satna',
            'Umaria', 'Sagar', 'Katni', 'Dewas', 'Indore', 'Morena',
            'Tikamgarh', 'Datia', 'Khargone', 'Singrauli', 'Sehore', 'Harda',
            'Shahdol', 'Seoni', 'Ashoknagar', 'Raisen', 'Shajapur', 'Panna',
            'Ratlam', 'East Nimar', 'Ujjain', 'Jabalpur'],
    'Maharashtra': ['Gadchiroli', 'Gondia', 'Kolhapur', 'Nagpur', 'Palghar', 'Thane',
            'Bhandara', 'Buldhana', 'Nanded', 'Parbhani', 'Osmanabad',
            'Raigad', 'Nandurbar', 'Yavatmal', 'Dhule', 'Hingoli', 'Latur',
            'Sindhudurg', 'Akola', 'Ahmednagar', 'Jalgaon', 'Pune', 'Nashik',
            'Amravati', 'Aurangabad', 'Beed', 'Washim', 'Chandrapur', 'Sangli'],
       
    'Manipur': ['Imphal West', 'Senapati', 'Noney'],
    'Meghalaya': ['East Khasi Hills', 'West Jaintia Hills', 'Ri Bhoi',
            'Eastern West Khasi Hills', 'South West Khasi Hills',
            'West Khasi Hills', 'South Garo Hills', 'West Garo Hills'],
       
    'Mizoram': ['Aizawl'],
    'Odisha': ['Cuttack', 'Sundargarh', 'Deogarh', 'Balangir', 'Boudh', 'Ganjam',
            'Koraput', 'Puri', 'Bargarh', 'Jharsuguda', 'Mayurbhanj',
            'Bhadrak', 'Dhenkanal', 'Malkangiri', 'Sambalpur', 'Anugul',
            'Rayagada', 'Gajapati', 'Nayagarh', 'Baleshwar', 'Sonepur',
            'Khordha', 'Kandhamal', 'Kendujhar','Bhubaneswar'],
    'Puducherry': ['Pondicherry'],
    'Punjab': ['Firozepur', 'Shahid Bhagat Singh Nagar', 'Fatehgarh Sahib',
            'Fazilka', 'Ludhiana', 'Gurdaspur', 'Pathankot', 'Rupnagar'],
       
    'Rajasthan': ['Kota', 'Sikar', 'Jodhpur'],
    'State/UT': ['District'],
    'Tamil Nadu': ['Thiruvallur', 'Tiruvannamalai', 'Thanjavur', 'Virudhunagar',
            'Perambalur', 'Ariyalur', 'Tiruppur', 'Madurai', 'Coimbatore',
            'Kallakurichi', 'Krishnagiri', 'Tiruchirappalli', 'Pudukkottai',
            'Thiruvarur', 'Dindigul', 'Salem', 'Sivaganga', 'Cuddalore',
            'Kanniyakumari', 'Dharmapuri', 'Mayiladuthurai', 'Kanchipuram',
            'Erode', 'Villupuram', 'Namakkal', 'Ranipet', 'Chengalpattu',
            'Tirupathur'],
    'Telangana': ['Peddapalli', 'Nirmal', 'Ranga Reddy', 'Suryapet',
            'Kumuram Bheem Asifabad'],
    'Uttar Pradesh': ['Jalaun', 'Chandauli', 'Bhadohi', 'Ballia', 'Faizabad', 'Fatehpur',
            'Unnao', 'Ghaziabad', 'Siddharth Nagar', 'Kannauj', 'Gorakhpur',
            'Bijnor', 'Lucknow', 'Hapur', 'Rae Bareli', 'Farrukhabad', 'Gonda',
            'Mirzapur', 'Jaunpur', 'Kasganj'],
    'Uttarakhand': ['Haridwar', 'Nainital', 'Rudraprayag'],
    'West Bengal': ['Purba Bardhaman', 'Birbhum', 'Howrah', 'Murshidabad',
            '24 Paraganas South', 'Nadia', 'Purulia', 'Hooghly',
            '24 Parganas South'],
}

def get_cities(request):
    state = request.GET.get('state')
    cities = STATE_CITY_MAP.get(state, [])
    return JsonResponse({'cities': cities})




DISEASE_ALL_TYPES = [
    "Acute Diarrheal Disease", "Leptospirosis", "Chickenpox", "Kyasanur Forest Disease", "Cholera",
    "Dog Bite", "Monkey Pox", "Fever with Rash", "Malaria", "Hepatitis-A", "Food Poisoning",
    "Scrub Typhus", "Dengue & Chikungunya", "Mumps", "Human Rabies", "Measles", "Chikungunya",
    "Hepatitis A", "Animal Bite - Dog Bite", "Dengue", "Jaundice", "Melioidosis", "Chicken Pox",
    "Diphtheria", "Hepatitis A&E", "Fever", "Shigellosis", "Typhoid", "Mushroom Poisoning",
    "Acute Diarrhoeal Disease", "Acute Hepatitis-A", "Acute Gastroenteritis", "Measles & Rubella",
    "Acute Encephalitic Syndrome", "Fever of Unknown Origin", "West Nile Fever", "Japanese Encephalitis",
    "Hepatitis E", "Food Poisoning (Mushroom Poisoning)", "Jaundice of < 4 weeks", "Anthrax",
    "Rubella", "Zika Virus", "Dysentery", "Scrub typhus", "Hepatitis A & E", "Mpox", "Nipah Virus",
    "CCHF", "Disease/Illness", "Hand Foot Mouth Disease (HFMD)", "Paratyphoid", "Others"
]

def get_disease(request):
    return JsonResponse({'disease': DISEASE_ALL_TYPES})


def testing(request):
    disease_name = request.GET.get('disease', 'Dengue')

    diseases = Disease.objects.filter(name__iexact=disease_name).select_related('trending_data')

    # Initialize time data with correct mappings
    time_data = {
        'monthly': {i: 0 for i in range(1, 13)},  # Months: 1 - 12
        'weekly': {i: 0 for i in range(1, 53)},   # Weeks: 1 - 52
        'yearly': 0,
    }

    state_data = defaultdict(int)

    for disease in diseases:
        trending = disease.trending_data
        if trending.created_at:
            created_at = localtime(trending.created_at)  # Convert to local timezone
            month = created_at.month  # 1 - 12
            week = created_at.isocalendar()[1]  # ISO Week Number (1 - 52)
            day = created_at.day  # 1 - 31

            # Assign cases correctly based on timestamps
            time_data['yearly'] += disease.cases
            time_data['monthly'][month] += disease.cases
            time_data['weekly'][week] += disease.cases

        state_data[trending.state] += disease.cases

    return JsonResponse({
        'timeData': {
            'monthly': time_data['monthly'],
            'weekly': time_data['weekly'],
            'yearly': time_data['yearly']
        },
        'stateData': {
            'states': list(state_data.keys()),
            'cases': list(state_data.values())
        }
    })
