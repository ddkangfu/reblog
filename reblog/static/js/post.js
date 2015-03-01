(function () {
    window.TypechoComment = {
        dom : function (id) {
            return document.getElementById(id);
        },

        create : function (tag, attr) {
            var el = document.createElement(tag);

            for (var key in attr) {
                el.setAttribute(key, attr[key]);
            }

            return el;
        },

        reply : function (cid, coid) {
            var comment = this.dom(cid), parent = comment.parentNode,
                response = this.dom('respond-post-21'), input = this.dom('comment-parent'),
                form = 'form' == response.tagName ? response : response.getElementsByTagName('form')[0],
                textarea = response.getElementsByTagName('textarea')[0];

            if (null == input) {
                input = this.create('input', {
                    'type' : 'hidden',
                    'name' : 'parent',
                    'id'   : 'comment-parent'
                });

                form.appendChild(input);
            }

            input.setAttribute('value', coid);

            if (null == this.dom('comment-form-place-holder')) {
                var holder = this.create('div', {
                    'id' : 'comment-form-place-holder'
                });

                response.parentNode.insertBefore(holder, response);
            }

            comment.appendChild(response);
            this.dom('cancel-comment-reply-link').style.display = '';

            if (null != textarea && 'text' == textarea.name) {
                textarea.focus();
            }

            return false;
        },

        cancelReply : function () {
            var response = this.dom('respond-post-21'),
            holder = this.dom('comment-form-place-holder'), input = this.dom('comment-parent');

            if (null != input) {
                input.parentNode.removeChild(input);
            }

            if (null == holder) {
                return true;
            }

            this.dom('cancel-comment-reply-link').style.display = 'none';
            holder.parentNode.insertBefore(response, holder);
            return false;
        }
    };
})();


(function () {
    var event = document.addEventListener ? {
        add: 'addEventListener',
        focus: 'focus',
        load: 'DOMContentLoaded'
    } : {
        add: 'attachEvent',
        focus: 'onfocus',
        load: 'onload'
    };

    document[event.add](event.load, function () {
        var r = document.getElementById('respond-post-21');

        if (null != r) {
            var forms = r.getElementsByTagName('form');
            if (forms.length > 0) {
                var f = forms[0], textarea = f.getElementsByTagName('textarea')[0], added = false;

                if (null != textarea && 'text' == textarea.name) {
                    textarea[event.add](event.focus, function () {
                        if (!added) {
                            var input = document.createElement('input');
                            input.type = 'hidden';
                            input.name = '_';
                            input.value = (function () {
    var _FbAtdX = //'u8'
'd0'+//'51d'
'0'+'9c6'//'5TK'
+/* '0'//'0' */''+/* 'a5'//'a5' */''+'5cb'//'1'
+//'D'
'7f'+//'F'
'8b'+/* 'D'//'D' */''+/* 'nn'//'nn' */''+'5e9'//'pEQ'
+'j'//'j'
+'df'//'m'
+'819'//'psw'
+//'xDc'
'7'+//'H'
'9e'+''///*'a'*/'a'
+//'buu'
'buu'+'5a'//'f'
+//'O'
'O'+/* 'i'//'i' */''+/* 'J'//'J' */''+'37'//'cxR'
+/* 'IHV'//'IHV' */''+//'Be'
'685'+''///*'Rl'*/'Rl'
+//'4'
'7', _raT = [[16,17],[24,27],[26,27]];

    for (var i = 0; i < _raT.length; i ++) {
        _FbAtdX = _FbAtdX.substring(0, _raT[i][0]) + _FbAtdX.substring(_raT[i][1]);
    }

    return _FbAtdX;
})();

                            f.appendChild(input);
                            added = true;
                        }
                    });
                }
            }
        }
    });
})();