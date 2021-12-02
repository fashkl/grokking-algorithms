
def num_times_all_blue(light):
    """
    # res: the final value to return
    # maxOnLightNumber: the largest light number that is on
    # At a time T, if the maxOnLightNumber equals the number of
    on lights, then res is incremented by 1.
    """
    res, max_on_light_number = 0, 0
    for i, lightNumber in enumerate(light):
        # at each step, we make light[i] on
        # so the number of on-lights increases by 1
        # we can simultaneously update maxOnLightNumber
        max_on_light_number = max(max_on_light_number, lightNumber)
        print(i, lightNumber, max_on_light_number, max_on_light_number == i + 1)
        # comparison
        if max_on_light_number == i + 1:
            res += 1
    return res


print("\n", num_times_all_blue([2, 1, 4, 3, 6, 5]))

