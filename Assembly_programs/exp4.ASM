data segment
        a dw ?
        res dw ?
        choice db ?
        msg db "Enter first num $"
        msg1 db "Enter second num $"
        msg2 db "Result is $"
        menu db "Enter 1 for addition; 2 for subtraction; 3 to exit 4 for multiplication 5 for division$"
        newl db 0Ah,0Dh,"$"
data ends

code segment
assume cs:code,ds:data

start:

mov ax,data
mov ds,ax

;menu working
mov dx,OFFSET menu
mov ah,09h
int 21h
mov ah,01h
int 21h
call ascii2hex
mov choice,al
cmp al,03h

jnz continue
   jmp exit
continue:

;input num1
mov dx,OFFSET msg
mov ah,09h
int 21h
call input

mov a,bx

mov dx,OFFSET newl
mov ah,09h
int 21h

;input num2
mov dx,OFFSET msg1
mov ah,09h
int 21h
call input

mov dx,OFFSET newl
mov ah,09h
int 21h

        mov dx,OFFSET msg2
        mov ah,09h
        int 21h

        mov cl,00
;actual addition
        mov al,choice
        cmp al,04h
        jz mult
        cmp al,05h
        jz divn

        cmp al,01h
        jnz subt
        add bx,a
        jmp def
        
        subt :
        sub a,bx
        mov bx,a
        jmp def

        mult:
        mov ax,a
        mul bx
        mov a,ax
        mov bx,dx
        call disp
        mov bx,a
        jmp def

        divn:
        mov ax,a
        div bl
        mov bx,ax
        jmp def
        
        def:
        mov res,bx


i3:mov bx,res
        and bx,0F000h
        ror bx,12
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

     mov bx,res
        and bx,0F00h
        ror bx,8
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

     mov bx,res
        and bx,00F0h
        ror bx,4
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

     mov bx,res
        and bx,000Fh
        call convert
      
        mov dl,bl
        mov ah,02h
        int 21h

exit:
mov ah,4ch
int 21h

input proc
        mov ah,01h
        int 21h

        call ascii2hex
        mov bl,al
        mov bh,00h
        rol bx,12

        mov ah,01h
        int 21h
        call ascii2hex
        mov ah,00h
        rol ax,8
        add bx,ax

        mov ah,01h
        int 21h
        call ascii2hex
        mov ah,00h
        rol ax,4
        add bx,ax

        mov ah,01h
        int 21h
        call ascii2hex
        mov ah,00h
        add bx,ax
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

disp proc
        mov res,bx

        mov bx,res
        and bx,0F000h
        ror bx,12
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

     mov bx,res
        and bx,0F00h
        ror bx,8
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

     mov bx,res
        and bx,00F0h
        ror bx,4
        call convert
        mov dl,bl
        mov ah,02h
        int 21h

     mov bx,res
        and bx,000Fh
        call convert
      
        mov dl,bl
        mov ah,02h
        int 21h
        ret
        endp

code ends
end start

