class MyCircularQueue {
    int[] arr;
    int k;
    int size;
    int front;
    int rear;

    public MyCircularQueue(int k) {
        this.k = k;
        arr = new int[k];
        this.size = 0;
        this.front = 0;
        this.rear = -1;
    }

    public boolean enQueue(int value) {
        if(size == k) return false;

        rear = (rear + 1) % k;
        arr[rear] = value;
        size++;

        return true;
    }

    public boolean deQueue() {
        if(size == 0) return false;

        front = (front + 1) % k;
        size--;

        return true;
    }

    public int Front() {
        if(size == 0) return -1;

        return arr[front];
    }

    public int Rear() {
        if(size == 0) return -1;

        return arr[rear];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == k;
    }
}