from multiprocessing import Process

def calculate(name):
    print(f"{name} started")
    total = 0
    for i in range(10_000_000):
        total += i
    print(f"{name} completed", total)

if __name__ == "__main__":
    process1 = Process(
        target=calculate,
        args=("Process 1",)
    )
    process2 = Process(
        target=calculate,
        args=("Process 2",)
    )
    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("All processes completed")
