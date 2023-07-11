function getRemainingTime(endTime) {
    const remainingTimeMs = endTime.getTime() - new Date().getTime();
    const remainingTimeSeconds = Math.floor(remainingTimeMs / 1000);
    const remainingDays = Math.floor(remainingTimeSeconds / (24 * 60 * 60));
    const remainingHours = Math.floor((remainingTimeSeconds % (24 * 60 * 60)) / (60 * 60));
    const remainingMinutes = Math.floor((remainingTimeSeconds % (60 * 60)) / 60);
    const remainingSeconds = Math.floor(remainingTimeSeconds % 60);
    return `${remainingMinutes} minutes, ${remainingSeconds} seconds`;
}

function getProgressPercentage(startTime, endTime) {
    const totalTimeMs = endTime.getTime() - startTime.getTime();
    const elapsedTimeMs = new Date().getTime() - startTime.getTime();
    return Math.floor((elapsedTimeMs / totalTimeMs) * 100);
}
