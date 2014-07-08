ASCII_CAP_A = 65
ASCII_CAP_Z = 90
ASCII_A = 97
ASCII_Z = 122
def rotx(x, string, encrypt=true)
  for i in 0..string.length - 1
  	ascii = string[i].ord
  	if encrypt 
      if ASCII_CAP_A <= ascii && ascii <= ASCII_CAP_Z
        encrypt_ascii = ascii + (x % 26)
        if encrypt_ascii > ASCII_CAP_Z
      	  encrypt_ascii = encrypt_ascii - ASCII_CAP_Z + ASCII_CAP_A - 1
        end	
      elsif ASCII_A <= ascii && ascii <= ASCII_Z
        encrypt_ascii = ascii + (x % 26)
        if encrypt_ascii > ASCII_Z
      	  encrypt_ascii = encrypt_ascii - ASCII_Z + ASCII_A - 1
        end
      else
        encrypt_ascii = ascii
      end
      string[i] = encrypt_ascii.chr
    else
      if ASCII_CAP_A <= ascii && ascii <= ASCII_CAP_Z
        decrypt_ascii = ascii - (x % 26)
        if decrypt_ascii < ASCII_CAP_A
      	  decrypt_ascii = decrypt_ascii + ASCII_CAP_Z - ASCII_CAP_A
        end	
      elsif ASCII_A <= ascii && ascii <= ASCII_Z
        decrypt_ascii = ascii - (x % 26)
        if decrypt_ascii < ASCII_A
      	  decrypt_ascii = decrypt_ascii + ASCII_Z - ASCII_A
        end
      else
        decrypt_ascii = ascii
      end
      string[i] = decrypt_ascii.chr
    end
  end
  p string
end

rotx 10, 'Hello, World'
rotx 36, 'Hello, World'
rotx 10, 'Rovvy, Hycvn', false
