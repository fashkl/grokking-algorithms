const sum = (arr) => {
    return arr.length === 0 ? 0 : arr[0] + sum(arr.slice(1))
}


