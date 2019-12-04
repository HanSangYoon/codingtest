str = "Marlin names this last egg Nemo, a name that Coral liked. \n" \
      "While attempting to save nemo, Marlin meets Dory, \n" \
      "a good-hearted and optimistic regal blue tang with short-term memory loss.\n" \
      "Upon leaving the East Australian Current,(888*%$^&%0928375)Marlin and Dory \n" \
      "NEMO leaves for school and Marlin watches NeMo swim away.\n" \
      "EOI"
lines = str.splitlines()
for line in lines:

    if 'nemo' in line.lower():
        print("Found")
    else:
        print("Missing")
