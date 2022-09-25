class FractionalKnapsack {

    var currentCapacity: Int = 200
    var valueOfBag: Int = 0
    val weightsOfItems: ArrayList<Int> = arrayListOf(10, 35, 40, 60, 70, 80, 90, 120)
    val valuesOfItems: ArrayList<Int> = arrayListOf(6, 2, 5, 7, 8, 2, 9, 1)

    fun fractionalKnapsack(): Int {
        val arrayOfValue = findMVPs(weightsOfItems, valuesOfItems)

        while (currentCapacity != 0) {

            val indexOfMaxValue = indexOfMaxValue(arrayOfValue)
            val itemWeight = weightsOfItems[indexOfMaxValue]
            val itemValue = valuesOfItems[indexOfMaxValue]

            weightsOfItems

            if (itemWeight <= currentCapacity) {
                // Adding complete item to bag
                currentCapacity -= itemWeight
                valueOfBag += itemValue
            } else if (itemWeight > currentCapacity) {
                // Adding partial item to bag
                valueOfBag += ((currentCapacity / itemWeight) * itemValue)
                currentCapacity = 0
            }

            // Removing the items from the lists
            arrayOfValue.remove(indexOfMaxValue)
            weightsOfItems.remove(indexOfMaxValue)
            valuesOfItems.remove(indexOfMaxValue)
        }
        return valueOfBag
    }

    private fun indexOfMaxValue(arrayOfValue: ArrayList<Int>): Int {
        var maxValue = -1
        var maxIndex = -1
        for (i in 0..arrayOfValue.size) {
            if (arrayOfValue[i] > maxValue) {
                maxIndex = i
            }
        }

        return maxIndex
    }

    private fun findMVPs(weightsOfItems: ArrayList<Int>, valuesOfItem: ArrayList<Int>): ArrayList<Int> {
        val arrayListOfMVP = arrayListOf(weightsOfItems.size)
        for (i in 0..weightsOfItems.size) {
            arrayListOfMVP.add(valuesOfItem[i] / weightsOfItems[i])
        }
        return arrayListOfMVP
    }

}