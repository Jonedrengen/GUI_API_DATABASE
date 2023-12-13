from database_requests import get_all_Persons, get_all_Sample, get_all_S_aureus, get_all_COVID19, get_all_Batch, get_all_Legionella, get_all_S_epidermidis, get_all_SequencedSample

def main():                         
    result = get_all_Sample()
    print(result[:10])
    print(type(result))

if __name__ == main():
    main()