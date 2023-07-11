var order = {
    start_time: '{{o.start_time.isoformat}}',
    total_time: '{{o.meal.cook_time}}' * 1000,
    elapse_time: Date.now() - start_time
}

function timeRemaining(totalTime, elapseTime){
    remainingTime = totalTime - elapseTime;
    remainingSeconds = Math.floor(remainingTime / 1000);
    return remainingSeconds + 'seconds'
}
