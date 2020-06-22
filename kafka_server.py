import producer_server


def run_kafka_server():
	# TODO get the json file path
    # EDITED BY LUKA 20.06.2020
    # which JSON is needed
    input_file = "./police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="com.luka.project2",
        bootstrap_servers="localhost:19092",
        client_id="com.luka.project2"
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()

    
# DONE 22.06.2020.