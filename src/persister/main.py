from manager import Manager

manager = Manager()

if __name__ == "__main__":
    try:
        print("Services Setup start...")
        manager.setup()
        print("Services Setup Complete...")
        print("Listening to Kafka ...")
        manager.listener()
    except Exception as e:
        print(e)
