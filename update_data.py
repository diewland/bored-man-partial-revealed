import json

# config
FROM_ID      = 1
TO_ID        = 200
IMAGE_IPFS   = 'https://diewland.github.io/bored-man-partial-revealed/assets'
#
INPUT_PATH   = '../bored-man/json_final'
OUTPUT_PATH  = './json'

# process each id
for id in range(FROM_ID, FROM_ID+TO_ID):

    # prepare paths
    src_path = "{}/{}.json".format(INPUT_PATH, id)
    dest_path = "{}/{}.json".format(OUTPUT_PATH, id)
    print("* {} -> IPFS* -> {}".format(src_path, dest_path))

    # load data
    data = json.load(open(src_path))

    # update new ipfs image
    data['image'] = "{}/{}.png".format(IMAGE_IPFS, id)

    # save to json destination
    with open(dest_path, "w") as f:
        json.dump(data, f)
