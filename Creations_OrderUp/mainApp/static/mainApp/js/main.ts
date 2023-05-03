// Define a function to calculate the remaining time between two dates
// function getRemainingTime(endTime: Date): string {
//     const remainingTimeMs = endTime.getTime() - new Date().getTime();
//     const remainingTimeSeconds = Math.floor(remainingTimeMs / 1000);
//     const remainingDays = Math.floor(remainingTimeSeconds / (24 * 60 * 60));
//     const remainingHours = Math.floor((remainingTimeSeconds % (24 * 60 * 60)) / (60 * 60));
//     const remainingMinutes = Math.floor((remainingTimeSeconds % (60 * 60)) / 60);
//     const remainingSeconds = Math.floor(remainingTimeSeconds % 60);
//     return `${remainingDays} days, ${remainingHours} hours, ${remainingMinutes} minutes, ${remainingSeconds} seconds`;
// }

// // Define a function to calculate the progress percentage
// function getProgressPercentage(startTime: Date, endTime: Date): number {
//     const totalTimeMs = endTime.getTime() - startTime.getTime();
//     const elapsedTimeMs = new Date().getTime() - startTime.getTime();
//     return Math.floor((elapsedTimeMs / totalTimeMs) * 100);
// }