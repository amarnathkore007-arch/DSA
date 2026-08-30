class Solution:
    def shipWithinDays(self, weights, days):

        # Minimum possible capacity
        low = max(weights)

        # Maximum possible capacity
        high = sum(weights)

        while low <= high:

            capacity = (low + high) // 2

            current_weight = 0
            required_days = 1

            # Ship packages in the given order
            for weight in weights:

                if current_weight + weight <= capacity:
                    current_weight += weight

                else:
                    # Start a new day
                    required_days += 1
                    current_weight = weight

            if required_days <= days:
                # Capacity works
                # Try a smaller capacity
                high = capacity - 1

            else:
                # Capacity is too small
                # Need a bigger capacity
                low = capacity + 1

        return low


# Function call
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

obj = Solution()

answer = obj.shipWithinDays(weights, days)

print(answer)