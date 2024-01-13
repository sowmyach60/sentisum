from elasticsearch import Elasticsearch,helpers
from Constants import SERVER_URL,USER_NAME,PASSWORD,FINGERPRINT,CSV_PATH1,CSV_PATH2,CSV_PATH3,INDEX
from SalaryCsvReaders import CsvReaderFormat1,CsvReaderFormat2,CsvReaderFormat3

def create_elasticsearch_client():
    return Elasticsearch(
        SERVER_URL,
        ssl_assert_fingerprint=FINGERPRINT,
        basic_auth=(USER_NAME, PASSWORD)
    )

def add_compensations_to_elasticsearch(es, compensations):
    actions = [
        {
            "_op_type": "index",
            "_index": INDEX,
            "_source": compensation.to_dict(),
        }
        for compensation in compensations
    ]
    helpers.bulk(es, actions)

def main():
    es = create_elasticsearch_client()
    print(es.info())

    compensations_from_csv1 = CsvReaderFormat1().read_csv(CSV_PATH1)
    compensations_from_csv2 = CsvReaderFormat2().read_csv(CSV_PATH2)
    compensations_form_csv3 = CsvReaderFormat3().read_csv(CSV_PATH3)

    all_compensations = compensations_from_csv1 + compensations_from_csv2 + compensations_form_csv3

    add_compensations_to_elasticsearch(es, all_compensations)

if __name__ == "__main__":
    main()
