function solution(bridge_length, weight, truck_weights) {
    const trucksOnB = []
    let weightOnB = 0
    let time = 0
    while (truck_weights.length || trucksOnB.length) {
        
        if (trucksOnB.length && (time - trucksOnB[0][0]) === bridge_length) {
            const [time, truckOut] = trucksOnB.shift();
            weightOnB -= truckOut;
        }
        
        if (weight - weightOnB >= truck_weights[0]) {
            const truckIn = truck_weights.shift();
            trucksOnB.push([time, truckIn]);
            weightOnB += truckIn;
        } else {
            if (trucksOnB.length) {
                time = bridge_length + trucksOnB[0][0] - 1
            }
        }
        
        time++;
    }
    
    return time;
}
console.log(solution(2, 10, [7, 4, 5, 6]))