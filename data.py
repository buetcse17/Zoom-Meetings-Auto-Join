week_day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

#Test Purpose
test_link = "https://us04web.zoom.us/j/78284168552?pwd=ZDRrcFJra3Z1TGY3YytSZUE3L1NSZz09"# add your test link
test_start = "18:25" # add your test start time
test_end = "18:26" # add your test end time


#Class Links
cse325_AI = "https://bdren.zoom.us/j/65725700491"
cse301_TM = "https://bdren.zoom.us/j/68649797763?pwd=aUF6ZW1rMHN3dVh5b2lPV1VFMlYvZz09"
cse321_AAI = "https://bdren.zoom.us/j/63310920931"
cse313_PSA = "https://bdren.zoom.us/j/63076981693?pwd=K0dZeFo0emdlVE0zSmkwU2hXdW1Kdz09"
cse317_SSE = "https://bdren.zoom.us/j/69661875989"



lst = [
    
    #SAT
    [cse313_PSA, "9:00", "9:50", "CSE-313", 'SAT'],
    [cse317_SSE, "10:00", "10:50", "CSE-317", 'SAT'],
    [cse325_AI, "11:00", "11:50", "CSE-325", 'SAT'],
    [cse301_TM, "12:00", "12:50", "CSE-301", 'SAT'],
    [test_link, test_start, test_end, "TEST-SAT", 'SAT'],
    
    #SUN
    [cse317_SSE, "9:00", "9:50", "CSE-317", 'SUN'],
    [cse321_AAI, "10:00", "10:50", "CSE-321", 'SUN'],
    [test_link, test_start, test_end, "TEST-SUN", 'SUN'],
    
    #MON
    [cse313_PSA, "9:00", "9:50", "CSE-313", 'MON'],
    [cse317_SSE, "10:00", "10:50", "CSE-317", 'MON'],
    [test_link, test_start, test_end, "TEST-MON", 'MON'],
    
    #TUE
    [cse321_AAI, "9:00", "9:50", "CSE-321", 'TUE'],
    [cse313_PSA, "10:00", "10:50", "CSE-313", 'TUE'],
    [cse301_TM, "11:00", "11:50", "CSE-301", 'TUE'],
    [cse325_AI, "12:00", "12:50", "CSE-325", 'TUE'],
    [test_link, test_start, test_end, "TEST-TUE", 'TUE'],
    
    #WED 
    [cse321_AAI, "10:00", "10:50", "CSE-321", 'WED'],
    [cse325_AI, "11:00", "11:50", "CSE-325", 'WED'],
    [cse301_TM, "12:00", "12:50", "CSE-301", 'WED'],
    [test_link, test_start, test_end, "TEST-WED", 'WED'],
]

