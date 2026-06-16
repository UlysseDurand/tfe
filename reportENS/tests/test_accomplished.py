from manual_build.accomplished import get_issues, get_prs 

def test_get_number_of_prs():
    result = get_prs()
    print(result[0]["fullName"], result[0]["prNb"])

def test_get_number_of_issues():
    result = len(get_issues())
    print(f"Issues: {result}")