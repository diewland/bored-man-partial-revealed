import json, shutil

# reveal range
FROM_ID      = 1
TO_ID        = 211

# ipfs
IMAGE_IPFS   = 'https://diewland.github.io/bored-man-partial-revealed/assets'

# json
INPUT_PATH   = '../bored-man/json_final'
OUTPUT_PATH  = './json'

# image
SRC_IMG_PATH = '../bored-man-assets-final'
DST_IMG_PATH = './assets'

# process each id
for id in range(FROM_ID, FROM_ID+TO_ID):

    # copy image file
    src_img = "{}/{}.png".format(SRC_IMG_PATH, id)
    dest_img = "{}/{}.png".format(DST_IMG_PATH, id)
    #print(src_img, '->', dest_img)
    shutil.copyfile(src_img, dest_img)

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
