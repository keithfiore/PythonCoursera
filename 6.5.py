# Write code using find() and string slicing (see section 6.10) to extract the number
# at the end of the line below. Convert the extracted value to a floating point number
# and print it out.
# You must actually pull the data from the string.

text = "X-DSPAM-Confidence:    0.8475"
fnd = text.find(":")
get_num = text[fnd+1:]
print(float(get_num))