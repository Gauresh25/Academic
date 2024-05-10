data segment
        msg db 0dh,0ah,"-- -- -- -- OF DF IF TF SF ZF -- AF -- PF -- CF $"
        newl db 0dh,0ah,"$"
        flag dw ?
data ends

code segment
ASSUME CS:Code,DS:Data
START:
        mov ax,Data
        mov ds,ax
        
        mov dx,offset msg
        mov ah,09h
        int 21h

        mov dx,offset newl
        mov ah,09h
        int 21h

        stc
        cli
        std     
        mov al,88h
        add al,88h

        pushf
        pop bx

        mov flag,bx

        mov cx,10h
        mov bx,8000h

 loops: mov ax,flag
 and ax,bx
 jz zero
 mov dl,31h
 mov ah,02h
 int 21h
 jmp space

 zero:mov dl,30h
  mov ah,02h
 int 21h

 space:mov dl,""
 mov ah,02h
 int 21h
 mov ah,02h
 int 21h
 ror bx,1

 loop loops

 mov ah,4ch
 int 21h
 code ends
end start
