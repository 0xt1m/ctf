undefined8 main(void)

{
  int random_integer;
  time_t current_time;
  long in_FS_OFFSET;
  uint positive_number;
  uint random_int_2;
  long i;
  FILE *flag_file;
  size_t file_size;
  void *memory_start;
  FILE *encrypted_flag_file;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag","rb"); // Open file to read bytes

  fseek(flag_file, 0, 2); // Takes pointer to the end of the file
  
  file_size = ftell(flag_file);

  fseek(flag_file, 0, 0); // Takes the pointer back to the beginning of the file

  memory_start = malloc(file_size); // Dedicates some memory and returns the address of the beginning of the dedicated memory

  fread(memory_start, file_size, 1, flag_file); // Read the whole file into a byte buffer

  fclose(flag_file); // close file



  current_time = time((time_t *)0x0); // Get current system time in unix

  positive_number = (uint)current_time; // convert current_time to unsigned int
  // Unsigned numbers can be only positive or zero
  // Basically making sure my number is positive

  // Encryption
  srand(positive_number); // Setting the seed for random number
  for (i = 0; i < (long)file_size; i = i + 1) {
    random_integer = rand(); // Random integer based on the seed
    *(byte *)((long)memory_start + i) = *(byte *)((long)memory_start + i) ^ (byte)random_integer;
    
    random_int_2 = rand();
    random_int_2 = random_int_2 & 7;
    //   0000000000001101  (13)
    // & 0000000000000111  (7)
    //   -------------------
    //   0000000000000101  (5)


    *(byte *)((long)memory_start + i) =
         *(byte *)((long)memory_start + i) << (sbyte)random_int_2 |
         *(byte *)((long)memory_start + i) >> 8 - (sbyte)random_int_2;
  }

  encrypted_flag_file = fopen("flag.enc", "wb");
  fwrite(&positive_number, 1, 4, encrypted_flag_file);
  fwrite(memory_start, 1, file_size, encrypted_flag_file);
  fclose(encrypted_flag_file);


  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;