data segment
        msg db "Enter first num $"
        msg2 db "Result is $"
       
data ends

code segment
assume cs:code,ds:data

start:

mov ax,data
mov ds,ax

;Input working
mov si,5000h
mov cl,05h

mov dx,OFFSET msg
mov ah,09h
int 21h
l1:call input
   mov [si],bl
   INC si
   DEC cl
   cmp cl,00h
   jnz l1

    mov si,5000h
    mov cl,05h
    mov al,[si]
  l2:  cmp al,[si]
       jc update
          mov al,[si]
                 
       update:inc si
       dec cl
       cmp cl,00h
       jnz l2
    
;output-------------
mov dx,OFFSET msg2
mov ah,09h
int 21h

mov bl,al
mov dh,bl
call convert
mov dl,bl
mov ah,02h
int 21h

mov bl,dh
and bl,0f0h
ror bl,04h

call convert
mov dl,bl
mov ah,02h
int 21h
mov bl,dh
and bl,0fh
call convert
mov dl,bl
mov ah,02h
int 21h


mov ah,4ch
int 21h        


input proc
        mov ah,01h
        int 21h

        call ascii2hex
        mov bl,al
        rol bl,4

        mov ah,01h
        int 21h
        call ascii2hex
       
       
        add bl,al

        ret
        endp

ascii2hex proc
        cmp al,41H
        jc num
        sub al,07h
        num:sub al,30h
        ret
        endp

convert proc
        cmp bl,0ah
        jc i1
        add bl,37h
        jmp i2
        i1:add bl,30h
        i2:ret
        endp

code ends
end start
